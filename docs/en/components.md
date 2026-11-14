# Architecture

The product is a set of clients and its own server stack of independent
services. Each service is responsible for one function.

```mermaid
flowchart TB
    subgraph Clients["Your devices and assistants"]
        APP["📱 Android<br/>full database on the device"]
        WEB["🌐 Web dashboard"]
        TG["💬 Telegram"]
        ASSIST["🤖 Claude, LM Studio<br/>and other MCP clients"]
    end

    subgraph Home["🏠 Your server"]
        GW{{"🚪 Gateway<br/>checks the pass"}}
        subgraph Write["Writes data"]
            AUTH["🔑 Sign-in and accounts"]
            LEDGER["📒 Ledger and sync"]
        end
        subgraph ReadOnly["Read-only"]
            REPORT["📊 Reports"]
            MCP["🔌 MCP server"]
            AI["✨ AI"]
        end
        BOT["💬 Bot"]
        DB[("🗄 Database")]
    end

    LLM["🧠 Language model<br/>on your own GPU"]
    NET["🌍 Internet: Google sign-in,<br/>exchange rates, Telegram"]

    APP -- "sync" --> GW
    WEB -- "dashboard" --> GW
    ASSIST -- "MCP + personal token" --> GW
    TG <-- "messages" --> BOT

    GW --> AUTH & LEDGER & REPORT & AI & MCP
    BOT --> LEDGER & REPORT & AI
    MCP --> REPORT
    AI --> LLM

    LEDGER == "writes" ==> DB
    REPORT -. "reads" .-> DB
    AUTH -.-> NET
    LEDGER -.-> NET
    BOT -.-> NET
```

Solid arrows are requests, the thick one is writing, dotted ones are reading
and rare calls to the internet. Everything inside the “Your server” frame runs
at your home.

## How an answer gets from the database to the assistant { #mcp-answer }

You ask Claude or LM Studio about your money — the model does not do the maths,
it calls a wallet tool and retells the ready-made figures:

```mermaid
sequenceDiagram
    autonumber
    actor U as You
    participant C as Claude / LM Studio
    participant G as Gateway
    participant M as MCP server
    participant R as Reports
    participant D as Database
    U->>C: “How much did I spend on cafés in summer vs winter?”
    C->>G: tool call + personal token
    G->>M: pass verified
    M->>R: report request (read-only)
    R->>D: the database does the sums
    D-->>R: monthly totals
    R-->>M: figures, period and currency
    M-->>C: tool result
    C-->>U: answer in plain words
```

Live examples of such answers are on the [“What it looks like”](showcase.md) page.

## Clients

| Component | Role |
|---|---|
| **Android app** | The main client: full database on the device, entry, reports, rates, AI, statement import |
| **Web dashboard** | Analytics, management of access, rates, currencies, settings and connections |
| **Telegram bot** | Quick expense entry, brief reports and questions |

## Server services

| Service | Function |
|---|---|
| **Gateway** | Single entry point: routes requests and checks the user's pass |
| **Sign-in and accounts** | Google sign-in, sessions and devices, roles, Telegram linking, MCP tokens |
| **Ledger and sync** | Stores wallets, categories and operations; accepts and distributes changes to devices; sharing and invitations; currencies, rates and icons |
| **Reports** | All calculations — balances, turnover, structure, trends, search. Read-only |
| **AI** | Parses expenses and statements, answers questions; the only component that talks to the language model; writes nothing |
| **MCP server** | Gives AI assistants wallet tools, read-only |
| **Bot** | Handles Telegram messages and acts on the user's behalf as one more device |

## Design principles

- **Writes and reads are separated.** Only the ledger service writes; reports
  read the same database with a role that cannot write.
- **One service issues passes**, the others verify them on their own. Each
  service gets only the rights it needs.
- **Batch sync**: a device sends its changes in one transaction and fetches
  everyone else's; resending never duplicates anything.
- **Observability**: metrics, logs, versions and self-describing APIs for
  every service.
