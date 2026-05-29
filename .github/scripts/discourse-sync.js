const https = require('https');
const {
  GH_TOKEN,
  GH_REPO_OWNER,
  GH_REPO_NAME,
  GH_CATEGORY_ID,
  DISCOURSE_URL,
} = process.env;
const DISCUSSION_TITLE = 'Top Forum Discussions This Week';
const TOPICS_TO_SHOW   = 3; 
const GH_GRAPHQL_URL   = 'https://api.github.com/graphql';

function fetch(url, options = {}) {
  return new Promise((resolve, reject) => {
    const req = https.request(url, options, (res) => {
      let body = '';
      res.on('data', chunk => body += chunk);
      res.on('end', () => {
        if (res.statusCode >= 400) {
          reject(new Error(`HTTP ${res.statusCode} for ${url}: ${body}`));
        } else {
          try { resolve(JSON.parse(body)); }
          catch { resolve(body); }
        }
      });
    });
    req.on('error', reject);
    if (options.body) req.write(options.body);
    req.end();
  });
}

function ghGraphQL(query, variables = {}) {
  const body = JSON.stringify({ query, variables });
  return fetch(GH_GRAPHQL_URL, {
    method: 'POST',
    headers: {
      'Content-Type':  'application/json',
      'Authorization': `bearer ${GH_TOKEN}`,
      'User-Agent':    'discourse-sync-action',
    },
    body,
  });
}
async function fetchDiscourseTopics() {
  console.log('Fetching top topics from Discourse…');
  const discourseHost = DISCOURSE_URL.replace('https://', '');
  const data = await fetch(`https://${discourseHost}/top.json?period=weekly`, {
    headers: { 'Accept': 'application/json', 'User-Agent': 'canton-gh-sync/1.0' },
  });
  const topics = (data?.topic_list?.topics || [])
    .filter(t => !t.pinned && t.id)  
    .slice(0, TOPICS_TO_SHOW);
  console.log(`  Found ${topics.length} topics`);
  return topics;
}
function buildBody(topics) {
  const date = new Date().toLocaleDateString('en-US', {
    weekday: 'long', year: 'numeric', month: 'long', day: 'numeric',
  });
  const rows = topics.map(t => {
    const url      = `${DISCOURSE_URL}/t/${t.slug}/${t.id}`;
    const replies  = t.posts_count > 1 ? `${t.posts_count - 1} replies` : 'No replies yet';
    const views    = t.views ? `${t.views.toLocaleString()} views` : '';
    const category = t.category_id ? `<!-- cat:${t.category_id} -->` : '';
    return `| [${t.title}](${url}) | ${replies} | ${views} |${category}`;
  }).join('\n');
  return `> Auto-updated every day from [forum.canton.network](${DISCOURSE_URL}) · Last synced **${date}**
Showing the most active threads from the past 7 days. Join the conversation on the forum — GitHub account not required.

| Thread | Replies | Views |
|--------|---------|-------|
${rows}

---

**[Browse all discussions →](${DISCOURSE_URL}/top?period=weekly)**
Want to start a thread? **[Post on the forum: ](${DISCOURSE_URL}/new-topic)**

---
*This post is automatically updated by the [discourse-sync](https://github.com/${GH_REPO_OWNER}/${GH_REPO_NAME}/blob/main/.github/workflows/discourse-sync.yml) GitHub Action.*`;
}
async function findExistingDiscussion() {
  console.log('Looking for existing Forum Highlights discussion…');
  const res = await ghGraphQL(`
    query($owner: String!, $name: String!) {
      repository(owner: $owner, name: $name) {
        discussions(first: 50, categoryId: "${GH_CATEGORY_ID}") {
          nodes { id title number }
        }
      }
    }
  `, { owner: GH_REPO_OWNER, name: GH_REPO_NAME });
  const nodes = res?.data?.repository?.discussions?.nodes || [];
  return nodes.find(d => d.title === DISCUSSION_TITLE) || null;
}

async function createDiscussion(body) {
  console.log('Creating new Forum Highlights discussion…');
  const repoRes = await ghGraphQL(`
    query($owner: String!, $name: String!) {
      repository(owner: $owner, name: $name) { id }
    }
  `, { owner: GH_REPO_OWNER, name: GH_REPO_NAME });

  const repoId = repoRes?.data?.repository?.id;
  if (!repoId) throw new Error('Could not fetch repo node ID');
  const res = await ghGraphQL(`
    mutation($repoId: ID!, $categoryId: ID!, $title: String!, $body: String!) {
      createDiscussion(input: {
        repositoryId: $repoId,
        categoryId:   $categoryId,
        title:        $title,
        body:         $body,
      }) {
        discussion { id number url }
      }
    }
  `, {
    repoId,
    categoryId: GH_CATEGORY_ID,
    title: DISCUSSION_TITLE,
    body,
  });
  const discussion = res?.data?.createDiscussion?.discussion;
  if (!discussion) {
    console.error('Create response:', JSON.stringify(res, null, 2));
    throw new Error('Failed to create discussion');
  }
  console.log(`  Created: ${discussion.url}`);
  return discussion;
}
async function updateDiscussion(id, body) {
  console.log('Updating existing Forum Highlights discussion…');
  const res = await ghGraphQL(`
    mutation($id: ID!, $body: String!) {
      updateDiscussion(input: { discussionId: $id, body: $body }) {
        discussion { id number url }
      }
    }
  `, { id, body });
  const discussion = res?.data?.updateDiscussion?.discussion;
  if (!discussion) {
    console.error('Update response:', JSON.stringify(res, null, 2));
    throw new Error('Failed to update discussion');
  }
  console.log(`  Updated: ${discussion.url}`);
  return discussion;
}

async function main() {
  if (!GH_TOKEN)       throw new Error('GH_TOKEN not set');
  if (!GH_CATEGORY_ID) throw new Error('GH_CATEGORY_ID not set');
  const topics    = await fetchDiscourseTopics();
  if (!topics.length) {
    console.log('No topics found — skipping.');
    return;
  }
  const body       = buildBody(topics);
  const existing   = await findExistingDiscussion();
  if (existing) {
    await updateDiscussion(existing.id, body);
  } else {
    await createDiscussion(body);
  }
  console.log('Done ✓');
}

main().catch(err => {
  console.error('Error:', err.message);
  process.exit(1);
});