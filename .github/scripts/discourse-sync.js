const https = require('https');
const {
  GH_TOKEN,
  GH_REPO_OWNER,
  GH_REPO_NAME,
  GH_CATEGORY_ID,
  DISCOURSE_URL,
} = process.env;

const TOPICS_TO_SHOW = 8;
const SYNC_TAG       = '<!-- discourse-sync -->'; 
const GH_GRAPHQL_URL = 'https://api.github.com/graphql';
function request(url, options = {}, body = null) {
  return new Promise((resolve, reject) => {
    const req = https.request(url, options, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        if (res.statusCode >= 400) {
          reject(new Error(`HTTP ${res.statusCode} → ${url}\n${data}`));
        } else {
          try { resolve(JSON.parse(data)); } catch { resolve(data); }
        }
      });
    });
    req.on('error', reject);
    if (body) req.write(body);
    req.end();
  });
}
function ghGraphQL(query, variables = {}) {
  const body = JSON.stringify({ query, variables });
  return request(GH_GRAPHQL_URL, {
    method: 'POST',
    headers: {
      'Content-Type':  'application/json',
      'Authorization': `bearer ${GH_TOKEN}`,
      'User-Agent':    'discourse-sync-action',
    },
  }, body);
}
async function fetchDiscourseTopics() {
  console.log('Fetching top topics from Discourse…');
  const host = DISCOURSE_URL.replace('https://', '');
  const data = await request(`https://${host}/top.json?period=weekly`, {
    headers: { 'Accept': 'application/json', 'User-Agent': 'canton-gh-sync/2.0' },
  });

  const topics = (data?.topic_list?.topics || [])
    .filter(t => !t.pinned && t.id)
    .slice(0, TOPICS_TO_SHOW);

  console.log(`  Found ${topics.length} topics`);
  return topics;
}
function buildTopicBody(topic) {
  const url     = `${DISCOURSE_URL}/t/${topic.slug}/${topic.id}`;
  const replies = topic.posts_count > 1 ? `${topic.posts_count - 1}` : '0';
  const views   = topic.views ? topic.views.toLocaleString() : '0';
  const date    = new Date().toLocaleDateString('en-US', {
    year: 'numeric', month: 'long', day: 'numeric',
  });

  return `${SYNC_TAG}
> This discussion is mirrored from **[forum.canton.network](${DISCOURSE_URL})** · Auto-synced on ${date}

**[Read & join the conversation on the forum →](${url})**

| | |
|---|---|
| Replies | ${replies} |
| Views | ${views} |

---

*Reacting here with 👍 shows community interest. To reply, head to the [forum thread](${url}) no GitHub account needed.*

${SYNC_TAG}`;
}
async function getRepoId() {
  const res = await ghGraphQL(`
    query($owner: String!, $name: String!) {
      repository(owner: $owner, name: $name) { id }
    }
  `, { owner: GH_REPO_OWNER, name: GH_REPO_NAME });
  const id = res?.data?.repository?.id;
  if (!id) throw new Error('Could not fetch repo node ID');
  return id;
}
async function fetchExistingDiscussions() {
  console.log('Fetching existing Forum Highlights discussions…');
  const res = await ghGraphQL(`
    query($owner: String!, $name: String!) {
      repository(owner: $owner, name: $name) {
        discussions(first: 50, categoryId: "${GH_CATEGORY_ID}") {
          nodes { id title body }
        }
      }
    }
  `, { owner: GH_REPO_OWNER, name: GH_REPO_NAME });
  const all = res?.data?.repository?.discussions?.nodes || [];
  return all.filter(d => d.body && d.body.includes(SYNC_TAG));
}
async function createDiscussion(repoId, title, body) {
  console.log(`  Creating: "${title}"`);
  const res = await ghGraphQL(`
    mutation($repoId: ID!, $categoryId: ID!, $title: String!, $body: String!) {
      createDiscussion(input: {
        repositoryId: $repoId,
        categoryId:   $categoryId,
        title:        $title,
        body:         $body,
      }) {
        discussion { id title url }
      }
    }
  `, {
    repoId,
    categoryId: GH_CATEGORY_ID,
    title,
    body,
  });
  const errors = res?.errors;
  if (errors) throw new Error(JSON.stringify(errors));
  const d = res?.data?.createDiscussion?.discussion;
  if (!d) throw new Error('createDiscussion returned null');
  console.log(`    → ${d.url}`);
  return d;
}
async function updateDiscussion(id, title, body) {
  console.log(`  Updating: "${title}"`);
  const res = await ghGraphQL(`
    mutation($id: ID!, $body: String!) {
      updateDiscussion(input: { discussionId: $id, body: $body }) {
        discussion { id url }
      }
    }
  `, { id, body });
  const errors = res?.errors;
  if (errors) throw new Error(JSON.stringify(errors));
}

async function main() {
  if (!GH_TOKEN)       throw new Error('GH_TOKEN not set');
  if (!GH_CATEGORY_ID) throw new Error('GH_CATEGORY_ID not set');
  const [topics, existing, repoId] = await Promise.all([
    fetchDiscourseTopics(),
    fetchExistingDiscussions(),
    getRepoId(),
  ]);
  if (!topics.length) {
    console.log('No topics found, skipping.');
    return;
  }
  const existingByTitle = {};
  existing.forEach(d => { existingByTitle[d.title] = d; });
  for (const topic of topics) {
    const title = topic.title;
    const body  = buildTopicBody(topic);
    if (existingByTitle[title]) {
      await updateDiscussion(existingByTitle[title].id, title, body);
    } else {
      await createDiscussion(repoId, title, body);
    }
    await new Promise(r => setTimeout(r, 500));
  }
  console.log(`\nDone & synced ${topics.length} topics`);
}

main().catch(err => {
  console.error('Error:', err.message);
  process.exit(1);
});