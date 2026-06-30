# Canton Developer Tooling Catalogue

A curated catalogue of tools, SDKs, APIs, and infrastructure available for building on Canton Network. Each entry includes what it does, who makes it, and where to find it.

> ***Disclaimer**: The tools, libraries, and resources labeled as 'Community' in this repository are submitted by third-party developers and ecosystem partners. They are not audited, endorsed, officially maintained, or guaranteed by the Canton Foundation. These resources are provided 'as is' for informational listing purpose only.*
> 
> *The Foundation assumes no liability for any security vulnerabilities, bugs, financial loss, or damages resulting from the use of these tools. Developers must do their own research and independently review the code and security of any third-party/Partner tools before integrating them into their projects.*

## Getting Started with BuidL

### Official Canton Network Documentation
![Official](https://img.shields.io/badge/Official-Digital_Asset-blue)

**What it is:** The authoritative technical documentation for Canton Network. Covers the Ledger API, Daml language, participant node setup, Canton Coin, Splice APIs, and more.

**Link:** [docs.canton.network](https://docs.canton.network)

### Canton Network API Overview
![Official](https://img.shields.io/badge/Official-Digital_Asset-blue)

**What it is:** A TL;DR overview of all the APIs available for building on Canton: Ledger API, JSON API, Admin API, Scan API, Validator API, and Wallet API. Start here to understand which API you need for what.

**Link:** [docs.canton.network/sdks-tools/api-reference/](https://docs.canton.network/sdks-tools/api-reference/)

### Canton 101
![Community](https://img.shields.io/badge/Community-Canton_Partner-D5A5E3)

**What it is:** A community built overview of Canton Network covering architecture, APIs, SDKs, and core concepts. Good first stop if you're completely new to Canton and want a lighter read before diving into the official docs.

**Link:** [canton-101.vercel.app](https://canton-101.vercel.app)


### DPM (Digital Asset Package Manager)
![Official](https://img.shields.io/badge/Official-Digital_Asset-blue)

**What it is:** The primary CLI tool for Canton/Daml development. `dpm` handles everything: initializing projects, building DARs, running tests, code generation (TypeScript and Java bindings), managing SDK versions, and running a local sandbox. If you're building a Daml project, you're using `dpm`.

**Key commands:**
```bash
dpm new           # scaffold a new project
dpm build         # compile Daml to .dar
dpm test          # run Daml Script tests
dpm sandbox       # run a local single node Canton environment
dpm codegen-js    # generate TypeScript bindings from your DAR
dpm codegen-java  # generate Java bindings from your DAR
dpm studio        # open project in VS Code with Daml extension
```

- **Repo:** [github.com/digital-asset/dpm](https://github.com/digital-asset/dpm)  

- **Docs:** [docs.canton.network/sdks-tools/cli-tools/dpm](https://docs.canton.network/sdks-tools/cli-tools/dpm)

### Daml Studio (VS Code Extension)
![Official](https://img.shields.io/badge/Official-Digital_Asset-blue)

**What it is:** The VS Code extension for Daml development. Gives you syntax highlighting, type checking, inline error diagnostics, and code navigation directly in your editor. Installed automatically when you install DPM. Launch it with `dpm studio` from your project directory.

**Link:** [marketplace.visualstudio.com](https://marketplace.visualstudio.com/items?itemName=DigitalAssetHoldingsLLC.daml)

**Requires:** VS Code 1.87 or above

### Canton Token Template by OpenZeppelin
![Community](https://img.shields.io/badge/Community-Canton_Partner-D5A5E3)

**What it is:** A Daml template for building CIP56 compliant token registries on Canton Network, from OpenZeppelin. If you're building a token or asset contract that needs to conform to the Canton Token Standard (CIP-056), this is the quickest starting point, clone it, run the setup script, and start writing your contracts on top.

**Repo:** [github.com/OpenZeppelin/canton-token-template](https://github.com/OpenZeppelin/canton-token-template)

### Catalyx Package Manager by IntellectEU
![Community](https://img.shields.io/badge/Community-Canton_Partner-D5A5E3)

**What it is:** A community built package marketplace for Canton/Daml components. Lets you discover, share, and consume reusable Daml packages across projects.

**Link:** [apps.catalyx.solutions/marketplace](https://apps.catalyx.solutions/marketplace)

### Tokenization Explorer by Catalyx
![Community](https://img.shields.io/badge/Community-Canton_Partner-D5A5E3)

**What it is:** A visual explorer for Canton tokenization workflows. Useful for prototyping and understanding how tokenised assets flow across Canton participants without building everything from scratch.

**Link:** [tokenization.catalyst.intellecteu.com](https://tokenization.catalyst.intellecteu.com/)

## AI Development Tools

### Tenzro DAML Studio: AI Browser IDE
![Community](https://img.shields.io/badge/Community-Canton_Partner-D5A5E3)

**What it is:** An AIpowered browser IDE for generating and editing Daml smart contracts. Useful for getting a starting point when you know what your contract should do but aren't yet fluent in Daml syntax. Also includes an agentic layer for DevNet interactions. Review and test all generated code before deploying.

**Link:** [tenzro.com/docs/canton](https://www.tenzro.com/docs/canton)

### Canton Dev MCP Server
![Official](https://img.shields.io/badge/Official-Canton_DevRel-blue)

**What it is:** A Model Context Protocol (MCP) server that plugs Canton's knowledge base directly into Claude (and other MCP compatible AI tools). Instead of AI hallucinating outdated Canton docs, the MCP server grounds responses in current, accurate Canton documentation covering the full dev stack from Daml to Ledger API to LocalNet. Especially useful at hackathons where you're using Claude to help write code.

**How it works:** Fetches a curated Canton knowledge base from GitHub on startup, caches it locally, and refreshes hourly. Works with Claude Desktop and any MCP- ompatible client.

**Repo:** [github.com/canton-network-devs/Build-on-Canton-MCP](https://github.com/canton-network-devs/Build-on-Canton-MCP)

## Local Development Environments

### Canton LocalNet (via cn-quickstart)
![Official](https://img.shields.io/badge/Official-Digital_Asset-blue)

**What it is:** A full Canton Network running locally in Docker Compose. Three validators (App Provider, App User, Super Validator), a local synchronizer, Canton Coin wallets, PQS, Keycloak auth, and Scan UI, all on your system. The go to environment for development and testing without needing DevNet access.

**When to use it:** Multi Party workflows, Canton Coin transfers, Wallet integration, Splice API testing, dApp development.

- **Repo:** [github.com/digital-asset/cn-quickstart](https://github.com/digital-asset/cn-quickstart)  

- **Guide:** See [LocalNet Deployment Guide](./cn_quickstart%20LocalNet%20Deployment%20Setup%20Guide.md), a walkthrough specifically for hackathon and bootcamp builders.


### Canton Sandbox (via DPM)
![Official](https://img.shields.io/badge/Official-Digital_Asset-blue)

**What it is:** A lightweight single node Canton environment for fast iteration on contract logic. No Docker required. Starts instantly. Good for unit-testing your Daml before you need the full LocalNet stack.

**When to use it:** Testing contract logic in isolation, Daml Script development, quick iteration without waiting for Docker.

```bash
dpm sandbox
```

### Seaport by 5North
![Community](https://img.shields.io/badge/Community-Canton_Partner-D5A5E3)

**What it is:** A cloud-based platform for coding, building, deploying, and managing Daml smart contracts, all in one place, without local setup. If you don't want to install the Daml SDK, Docker, and the whole local toolchain, Seaport gives you a managed environment from development through to production.

**Link:** [devnet.seaport.to](https://devnet.seaport.to/)

## Language SDKs & Client Libraries

### Go SDK for Daml Ledger by Noders
![Community](https://img.shields.io/badge/Community-Canton_Partner-D5A5E3)

**What it is:** A comprehensive Go SDK for interacting with Canton/Daml ledgers. Includes a complete Ledger API client library, service abstractions, and a code generator that produces type-safe Go code from your `.dar` files. Also includes a separate wallet SDK for building wallet applications on Canton using Splice Amulet protocol. If your backend is Go, this is your starting point.

**Repos:**
- Ledger SDK: [github.com/noders-team/go-daml](https://github.com/noders-team/go-daml)
- Wallet SDK: [github.com/noders-team/go-wallet-daml](https://github.com/noders-team/go-wallet-daml)

### C7 Ledger & C7 React by C7 Digital
![Community](https://img.shields.io/badge/Community-Canton_Partner-D5A5E3)

**What it is:** Drop-in replacements for the official `@daml/ledger` and `@daml/react` packages. `@c7/ledger` and `@c7/react` give you the same API for connecting JavaScript/TypeScript frontends and backends to the Daml Ledger API, with active maintenance from C7 Digital. Worth evaluating alongside the official DA packages if you're building a React or Node.js frontend on Canton.

**Repo:** [github.com/C7-Digital/c7_ledger](https://github.com/C7-Digital/c7_ledger)

## APIs

### JSON Ledger API
![Official](https://img.shields.io/badge/Official-Digital_Asset-blue)

**What it is:** An HTTP/JSON interface to the Canton Ledger API. Submit commands (create contracts, exercise choices), query active contracts, and stream events all over standard HTTP. The easiest way to integrate a backend or test scripts with Canton without setting up gRPC.

**Docs:** [docs.canton.network/sdks-tools/api-reference/json-api](https://docs.canton.network/sdks-tools/api-reference/json-api)

### gRPC Ledger API
![Official](https://img.shields.io/badge/Official-Digital_Asset-blue)

**What it is:** The full Ledger API over gRPC/Protobuf. More powerful and higher-performance than the JSON API. Required for production backends and streaming event subscriptions. Use code generation (`dpm codegen-java` or `dpm codegen-js`) to get typed client bindings.

**Docs:** [docs.canton.network/sdks-tools/api-reference/ledger-api-services](https://docs.canton.network/sdks-tools/api-reference/ledger-api-services)

### Scan API
![Official](https://img.shields.io/badge/Official-Digital_Asset-blue)

**What it is:** A read-only API for querying network level Canton data, mining rounds, Canton Coin supply, featured apps, and DSO governance state. Think of it as a public read API for the Global Synchronizer.

**Docs:** [docs.canton.network/sdks-tools/api-reference/splice-scan-api](https://docs.canton.network/sdks-tools/api-reference/splice-scan-api)

### Validator API
![Official](https://img.shields.io/badge/Official-Digital_Asset-blue)

**What it is:** REST APIs exposed by each validator node for wallet operations, traffic management, party onboarding, and Canton Coin transfers. This is what the wallet UIs talk to under the hood.

**Docs:** [docs.canton.network/sdks-tools/api-reference/splice-validator-api](https://docs.canton.network/sdks-tools/api-reference/splice-validator-api)

## Data Explorer & Indexing

### PQS (Participant Query Store)
![Official](https://img.shields.io/badge/Official-Digital_Asset-blue)

**What it is:** A PostgreSQL-backed query store that mirrors your participant's ledger state and lets you run SQL queries against it. Essential for any app that needs complex queries, aggregations, or reporting on contract data. LocalNet includes PQS instances for both App Provider and App User out of the box.

**When to use it:** Complex contract queries, reporting, dashboards, anything where the Ledger API's streaming model is too limited.

**Docs:** [docs.canton.network/sdks-tools/development-tools/pqs](https://docs.canton.network/sdks-tools/development-tools/pqs)

### CCView Explorer & Indexing API by PixelPlex
![Community](https://img.shields.io/badge/Community-Canton_Partner-D5A5E3)

**What it is:** A community built Canton Network block explorer with a public indexing API, built by PixelPlex. Browse Canton transactions and network activity via the explorer. The indexing API lets you pull Canton on chain data into your own application, covering ANS lookups, transaction history, and more.

**Explorer:** [ccview.io](https://ccview.io)  
**API Docs:** [docs.ccview.io/reference/ans](https://docs.ccview.io/reference/ans)

### Lighthouse Explorer
![Community](https://img.shields.io/badge/Community-Canton_Partner-D5A5E3)

**What it is:** Another community built Canton Network explorer, providing an alternative view into network activity and transactions.

**Link:** [lighthouse.cantonloop.com](https://lighthouse.cantonloop.com)

## Wallet Integration

### Canton Wallets
![Official](https://img.shields.io/badge/Official-Canton_Network-blue)

**What it is:** A growing ecosystem of wallets, retail, enterprise, self custody, and custodial that support Canton Network assets and Canton Coin. If your app needs users to hold or transfer CC or other Canton assets, your users will interact through one of these.

**Full list:** [cantonecosystem.com](https://www.cantonecosystem.com/)

### Wallet <> dApp Development Kit (Wallet Gateway)
![Official](https://img.shields.io/badge/Official-Digital_Asset-blue)

**What it is:** An opensource SDK for building dApps that integrate with Canton wallets. Includes the dApp API spec (OpenRPC) and a dApp SDK for connecting your frontend to Canton wallet functionality.

**Repo:** [github.com/canton-network/wallet-gateway](https://github.com/canton-network/wallet-gateway/tree/main)  

### WalletConnect Integration for Canton
![Community](https://img.shields.io/badge/Community-Canton_Partner-D5A5E3)

**What it is:** WalletConnect integration for Canton Network, connect your dApp to any WalletConnect-compatible wallet that supports Canton.

**docs:** [docs.walletconnect.network](https://docs.walletconnect.network/wallet-sdk/chain-support/canton)

### Console dApp SDK by PixelPlex
![Community](https://img.shields.io/badge/Community-Canton_Partner-D5A5E3)

**What it is:** An npm package for integrating the Console Wallet into your Canton dApp. Lets your frontend connect to users' Console Wallet for signing and submitting transactions.

**npm:** [@console-wallet/dapp-sdk](https://www.npmjs.com/package/@console-wallet/dapp-sdk)

### Loop SDK by 5North
![Community](https://img.shields.io/badge/Community-Canton_Partner-D5A5E3)

**What it is:** An SDK for integrating the Loop Wallet into your Canton dApp frontend. Lets your app connect to users' Loop Wallet for Canton Coin and asset management.

**Docs:** [docs.fivenorth.io](https://docs.fivenorth.io/)

## Identity Verification SDK

### Five North ID SDK
![Community](https://img.shields.io/badge/Community-Canton_Partner-D5A5E3)

**What it is:** An identity verification SDK for Canton applications. Integrates tamper-proof KYC/identity checks into your Canton dApp, relevant for regulated industries where user identity verification is a requirement.

**Docs:** [docs.fivenorth.io/id-sdk/introduction](https://docs.fivenorth.io/id-sdk/introduction/)


> *This catalogue is maintained by [Jatin](https://x.com/Jpandya26), Developer Relations Manager, Canton Foundation. To Suggest Additions or Corrections, Open a PR or raise an issue in this repo.*
