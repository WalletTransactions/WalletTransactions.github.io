# AI assistants (MCP)

Connect your wallet to **LM Studio, Claude** or any other client that
supports the [Model Context Protocol](https://modelcontextprotocol.io) — and
ask about your money in the assistant you already use.

## How to connect

1. Issue a **personal MCP token** in the web dashboard.
2. Enter the MCP server address and the token in your client.
3. Ask: "how much did I spend in cafés this summer compared with winter?"

## What it can do

| Tool | Purpose |
|---|---|
| `list_wallets` | List of wallets |
| `list_categories` | List of categories |
| `balance` | Balances on a date |
| `spending_by_category` | Spending by category for a period, with period comparison |
| `spending_by_category_by_month` | Monthly spending by category, monthly average, seasonality |
| `income_expense_by_month` | Income and expenses by month |
| `search_operations` | Text search over operations, with a total |

## Guarantees

- **Read-only** — nothing can be changed through MCP.
- **The database does the maths**, not the model: the assistant gets ready
  totals together with the period and currency they were computed for.
- The token can be **revoked** at any time; on every request it is swapped
  for a short-lived pass that can only read reports.
