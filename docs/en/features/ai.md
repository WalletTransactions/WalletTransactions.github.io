# AI assistant

!!! info "The golden rule"
    The AI **only suggests**. Every expense and every statement line arrives
    as a draft, and only what you have reviewed and confirmed with a button
    goes into your wallet.

## Expenses in your own words

> "taxi 450 yesterday from my Tinkoff card"

The AI extracts the amount, date, currency, wallet and category — **only from
your own** wallets and categories. If there are several candidates, it asks.
Where to enter:

- in the app — as text, by **voice**, or via "Share" from another app (for
  example, a forwarded bank SMS);
- on the web — on the "AI" screen;
- in Telegram — just send the bot a message.

## Bank statement import { #statement-import }

1. Hand over a PDF or CSV from your banking app ("Share" or file picker) and
   choose a wallet.
2. Parsing runs in the background: progress is visible, you can cancel, and
   you can close the app — the work continues.
3. Every amount and date is checked by **literal match against the
   document** — the model cannot "invent" an operation.
4. Categories are picked first by your own rules, then by the merchant
   description. Where neither is confident, you decide.
5. Lines that are already in the wallet are flagged as duplicates.
6. Review the list, fix what you need and save — one by one or all ready
   lines at once.

Popular banks have built-in format profiles, and your corrections gradually
train a personal profile.

## Questions about money

> "How much did I spend on food and the nanny in September?"

The bot tells a question from an expense and answers in a short dialogue with
follow-ups. Numbers come from server reports; the model only retells them.
Model choice: **local** (data never leaves the server) or a cloud one — only
with your explicit consent.
