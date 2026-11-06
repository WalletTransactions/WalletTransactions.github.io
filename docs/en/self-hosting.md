# Your own server at home

!!! tip "Your money on your hardware"
    The Count & Save server runs **in your home** — on an old laptop, a mini
    PC or a home server. No clouds, no third-party data centers: the
    database, the reports and even the language model run on your computer.

## Why at home

- **Your data stays put.** Operations, balances and statements live in a
  database on your computer. Neither the developer, nor a hosting company,
  nor a cloud provider can see them.
- **AI at home, too.** Expenses and statements are parsed by a **local
  language model** on your graphics card. "Taxi 450 yesterday" and your bank
  PDF are never sent to someone else's neural network.
- **No subscriptions.** No monthly cloud bill and no risk of the service
  shutting down and taking your data with it.
- **Full control.** Backups, updates, who has access — you decide.

## A server is optional

The Android app is complete bookkeeping **with no server at all**: all data
on the phone, works on a plane and in the countryside. A home server adds
what needs a "second computer":

| Without a server | With a home server |
|---|---|
| ✅ Tracking, reports, rates, recurring operations on the phone | ✅ All of the same |
| ✅ Manual JSON backup | ✅ Automatic sync — a copy is always on the server |
| — | ✅ Several phones and a shared family wallet |
| — | ✅ Web dashboard with big-screen analytics |
| — | ✅ Telegram bot |
| — | ✅ AI: expenses in plain words, statement import, questions about money |
| — | ✅ AI assistants over MCP |

## What you need

| | Minimum | For AI features |
|---|---|---|
| **Computer** | Any PC, mini PC or laptop with Linux and Docker that can stay on | Same |
| **Graphics card** | Not needed | GPU with 8 GB of VRAM (e.g. GTX 1070) for models up to 8B |
| **Network** | Home Wi-Fi | Same |

Without a GPU the server works fully; AI features are simply hidden in the
app, on the web and in the bot. Add a GPU later and AI switches on by itself.

## How it works

- The whole server is **one set of containers** (`docker compose`): a
  PostgreSQL database, the ledger, reports, sign-in and AI services, the web
  dashboard and the bot. One command to start, a version bump to update.
- The **language model** runs next to it in [LM Studio](https://lmstudio.ai)
  on the same computer.
- The **phone** connects to the server by its home network address: "More" →
  "Integrations". Sync runs in the background as soon as the phone is home.
  Away from home the phone keeps working offline and catches up when you
  return — or through your own VPN.

## What still goes to the internet { #internet }

An honest list, so that "no clouds" is not an exaggeration:

| What | Why | Can you do without it? |
|---|---|---|
| **Google sign-in** | Confirms it is you. Google learns only that you signed in, not your finances | Required for sign-in |
| **Exchange rates** (ECB, Bank of Russia, Yahoo Finance) | Rate download on request | Yes — rates can be entered manually |
| **Telegram** | The bot works through Telegram's servers; Telegram sees messages to the bot | Yes — the bot is optional |
| **Cloud model** (Claude) | Only if you choose it over the local one | Yes — off by default |

The wallet data itself — operations, balances, statements — is stored and
processed only on your server.

!!! note "Installation guide"
    A step-by-step guide and a ready-made home installation kit are
    [in development](roadmap.md).
