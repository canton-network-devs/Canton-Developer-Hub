# Canton Developer Hub

A community resource maintained by the **Canton Foundation**. This repo is the starting point for developers and builders coming to Canton Network, whether you're at a hackathon, a bootcamp, or just exploring what Canton can do.

## The Developer Path

Not sure where to start? Here's something help:

| Where you are | What to use |
|---|---|
| "I have a .DAR file built of my Daml Contracts using `dpm`, I need a Canton LocalNet right now to deploy and show my project demo" | **[Canton Builder Tool](https://github.com/canton-network-devs/Canton-Builder-Tool)** |
| "I want to understand LocalNet along with a sample backend, frontend, keyclock, use PQS to Index, etc" | **[CN_Quickstart LocalNet Deployment Guide](https://canton-network-devs.github.io/Canton-Builder-Tool/#qs-model:~:text=PART%202%20%E2%80%94%20FULL%20CONTROL)** |
| "I want to build a same fullstack Canton dApp first with backend, auth, frontend to learn" | **[cn-quickstart](https://github.com/digital-asset/cn-quickstart)**

Each tier is a natural next step from the previous one. Start fast, go deeper as you need to.

## What's Here for Builders then?

### [Canton Dev Toolings Catalogue](https://dev-hub.canton.foundation/) 

A structured catalogue and guide of Tools, SDKs, APIs, and Pieces of infrastructure available for building on Canton. It Covers:

- Smart Contract Tools (DPM, VS Code extension, etc)
- AI development tools (Canton MCP Server, Tenzro DAML Studio)
- Local development environments (LocalNet, Sandbox)
- APIs (JSON Ledger API, gRPC, Scan, Validator)
- Data & indexing (PQS, CCView, Lighthouse)
- Wallet integration and identity SDK

Each tool is tagged as **Official** (Digital Asset OR Canton Foundation) or **Community** (Canton Ecosystem Partners) so you know what you're working with.

### [Canton Builder Tool: Easy LocalNet Setup](https://github.com/canton-network-devs/Canton-Builder-Tool)

The easy and stright way to get a full Canton Network running on your system without manual setup and deploy your .DARs on Canton LocalNet.

```bash
# Install
curl -fsSL https://raw.githubusercontent.com/canton-network-devs/Canton-Builder-Tool/main/install.sh | bash
 
# Start a full Canton Network locally
canton builder start
 
# Deploy your DAR
canton builder deploy ./your-project.dar
```

This Gets you 3 validators(app_user, app_providor, and SV), local synchronizer, Canton Coin wallets on Localhost, Local Scan UI, Local Ledger APIs and other useful full official Splice Canton LocalNet stack.

### [cn_quickstart LocalNet Deployment Guide](https://canton-network-devs.github.io/Canton-Builder-Tool/#qs-model:~:text=PART%202%20%E2%80%94%20FULL%20CONTROL)

Guide to getting your Daml project running on cn_quickstart based Canton LocalNet with wallets, multi-party transactions, etc. Built specifically for participants who need to plug their project properly into ***cn_quickstart***, use PQS, interact with wallets via the JSON API, and more. Use this when **Canton DevRel Tool** isn't enough and you want full control OVER a localnet stack.

It Covers:

- What LocalNet actually is
- Prerequisites and exact setup steps
- How to plug your own Daml project into cn-quickstart
- Uploading your DAR and discovering party IDs
- Creating contracts via the JSON API
- Tapping CC and testing wallet transfers

**System:** macOS and Linux. Windows: use WSL.

## What is Canton Network?

Canton Network is a **privacy-first blockchain** built for institutional and enterprise use cases. Unlike traditional public blockchains where all transactions are visible to everyone, Canton gives parties selective visibility i.e you only see what you're authorized to see, at the protocol level.

Key properties:

- **Need to know privacy**: data is shared only with parties who are signatories or observers on a contract. This is enforced by the protocol, not by operator configuration.

- **Daml smart contracts**: business logic written in a functional, strongly-typed language designed for multi-party workflows

- **Canton Coin**: the network's utility token, used to pay for transaction traffic

- **Global Synchronizer**: coordinates cross participant transactions without a shared global state and fully encrypted.

## Quick Start for Hackathon Builders

Done Coding your Daml contracts and a `.dar` file via `dpm` ? Go straight to either The **[Canton Builder Tool](https://github.com/canton-network-devs/Canton-Builder-Tool)** or **[cn_quickstart LocalNet Deployment Guide](NEW LINK)**.

#### Starting from scratch?

1. Install DPM: [docs.canton.network/sdks-tools/cli-tools/dpm](https://docs.canton.network/sdks-tools/cli-tools/dpm)
2. Scaffold a project: `dpm new <PROJECT NAME> --template empty-skeleton`
3. Write your Daml contracts, build with `dpm build` and test with `dpm test`
4. Use **[Canton Builder Tool](https://github.com/canton-network-devs/Canton-Builder-Tool)** or Follow the **[cn_quickstart LocalNet Deployment Guide](https://canton-network-devs.github.io/Canton-Builder-Tool/#qs-model:~:text=PART%202%20%E2%80%94%20FULL%20CONTROL)** to deploy

> *Maintained by Developer Relations, Canton Foundation*