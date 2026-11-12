# Services overview

The product is made of eight business services. Each one is available in one
or more clients.

| Service | What you get | 📱 Android | 🌐 Web | 💬 Telegram | 🤖 AI assistant |
|---|---|:-:|:-:|:-:|:-:|
| [Money tracking](features/accounting.md) | Wallets, categories, income, expenses, transfers, capital, recurring operations | ✅ | ✅ | ✅ expense entry | — |
| [Currencies and rates](features/currencies.md) | Any currency, pairs, rate history and import, equivalent totals | ✅ | ✅ | — | — |
| [Reports and analytics](features/reports.md) | Structure, trends, balances, operations feed, period comparison | ✅ | ✅ full | ✅ brief | ✅ |
| [AI assistant](features/ai.md) | Expenses in plain words, statement import, questions about money | ✅ | ✅ | ✅ | — |
| [Shared wallet](features/sharing.md) | Invite by link, roles, ownership transfer | ✅ sync | ✅ management | — | — |
| [Telegram bot](features/telegram.md) | Quick entry and lookup without the app | — | linking | ✅ | — |
| [MCP for AI assistants](features/mcp.md) | Ask about your spending from LM Studio, Claude and others | — | token issuing | — | ✅ |
| Account and devices | Google sign-in, active sessions, remote sign-out, account deletion | ✅ | ✅ | — | — |

## Cross-cutting principles

**Your own server at home.**
:   All server services and the language model run on your computer at
    home, not in a cloud. [Learn more](self-hosting.md).

**Offline first.**
:   The phone is a full client with its own database. The server is there for
    backup, other devices, the web, the bot and AI.

**One data set, many entry points.**
:   The app, the web dashboard and the bot all write through the same sync
    protocol, so an operation entered in Telegram shows up on the phone and on
    the web right away.

**AI never writes to your wallet.**
:   Every AI result is a draft. The client saves it only after the user
    explicitly confirms.

**The database does the maths.**
:   Answers about money are based on server reports; the model only phrases
    the answer.

**Deletion means deletion.**
:   Users delete their account and all data themselves from the settings.
