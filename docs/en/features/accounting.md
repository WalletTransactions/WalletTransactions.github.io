# Money tracking

## Wallets and categories

- **Wallet** — where the money is: a card, cash, a deposit, a brokerage
  account. A wallet has a currency and a balance.
- **Category** — an income or expense item: "Food", "Taxi", "Salary".
- Custom **icons** for wallets and categories — from the shared set or from
  your phone gallery, with cropping.
- **Archive** — an old wallet disappears from the entry pickers but still
  counts in balances and reports.

## Operations

| Type | How it works |
|---|---|
| **Expense** | Wallet → category |
| **Income** | Category → wallet |
| **Transfer** | Wallet → wallet, counted as neither income nor expense |
| **Transfer with conversion** | Between wallets in different currencies: each side in its own currency, the rate is fixed by the operation itself |
| **Fee** | Attached to a transfer and counted as an expense |

- Filter the feed by period, wallets and categories.
- A wallet balance is never stored — it is always recomputed from operations,
  so it never drifts.

## Capital

An apartment, a car, a renovation are investments, not expenses. A wallet can
be marked as a **capital asset** (real estate, a car or other):

- the purchase and further investments are **transfers** into the asset, so
  they do not inflate expenses;
- **revaluation** is a separate entry: the asset went up or down in value,
  while income and expenses stay the same;
- reports show liquid money and capital separately, plus a "total including
  capital"; for each asset you see the invested amount, revaluation and
  return.

Assets are created and revalued in the app; the web dashboard has a
"Capital" section.

## Recurring operations

Subscriptions, rent, salary: a scheduled rule creates operations by itself.
Toggle it on and off with a single switch.

## Reminder

Once a day at the time you choose, the app reminds you to enter your
expenses — but only if you have not entered anything today and the app is not
open.

## Import and export

- Full database export and import in JSON.
- Moving from **Money Lover**: a converter turns its export into the import
  format.
- **Bank statement** import (PDF and CSV) with AI — see
  [AI assistant](ai.md#statement-import).
