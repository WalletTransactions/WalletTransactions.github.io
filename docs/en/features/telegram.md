# Telegram bot

The bot is one more of your "devices": whatever you record in it instantly
appears in the app and on the web.

## Linking

In the web dashboard, on the "Access and invitations" screen, get a one-time
code and send it to the bot. You can unlink at any time — from the bot or
from the web.

## Entering expenses

- **Strict format** — a single line that always works, even without AI.
- **Your own words** — "coffee 200", "taxi 450 yesterday from Tinkoff".
- The bot picks a wallet and a category, asks with buttons when unsure and
  shows a **confirmation card**. Nothing is saved until you tap.
- Tapping twice does not create a duplicate.

## Commands

| Command | What it does |
|---|---|
| `/wallets` | Wallets with balances |
| `/categories` | Categories |
| `/last` | Recent operations |
| `/default` | Default wallet |
| `/tz` | Time zone |
| `/unlink` | Unlink the bot |

## Questions

Ask in your own words — the bot answers from your wallet data and asks for
clarification if the question is ambiguous. The model is local or cloud, your
choice.
