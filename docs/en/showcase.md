# What it looks like

The screenshots use demo data: two wallets and about a year of transactions with
seasonal spending. They contain no real amounts, names or addresses. Where to
get each client is on the [“Platforms”](platforms.md) page; what it is all made
of is in [“Architecture”](components.md).

=== "📱 Android"

    The app works offline and syncs in the background. The four screens of the
    bottom navigation:

    <div style="display:flex;flex-wrap:wrap;gap:1rem;justify-content:center" markdown>

    <figure style="max-width:240px;margin:0" markdown>
    ![Operations screen: the transaction feed for the period and a summary card](assets/shots/android-operations.png){ loading=lazy }
    <figcaption>Operations — the feed for the period and totals on top.</figcaption>
    </figure>

    <figure style="max-width:240px;margin:0" markdown>
    ![Wallets screen: two wallets with their balances](assets/shots/android-wallets.png){ loading=lazy }
    <figcaption>Wallets — the balance of each account.</figcaption>
    </figure>

    <figure style="max-width:240px;margin:0" markdown>
    ![Reports screen: spending by category for the selected period](assets/shots/android-reports.png){ loading=lazy }
    <figcaption>Reports — where the money goes, by category.</figcaption>
    </figure>

    <figure style="max-width:240px;margin:0" markdown>
    ![More screen: reference lists and settings](assets/shots/android-more.png){ loading=lazy }
    <figcaption>More — reference lists, debts, rates and settings.</figcaption>
    </figure>

    </div>

=== "🌐 Web dashboard"

    The web dashboard is adapted to phones: the same reports and the transaction
    list open in a browser with nothing to install. The screenshots are taken at
    a mobile width.

    <div style="display:flex;flex-wrap:wrap;gap:1rem;justify-content:center" markdown>

    <figure style="max-width:280px;margin:0" markdown>
    ![Web dashboard: spending report](assets/shots/web-report.png){ loading=lazy }
    <figcaption>The spending report for a period.</figcaption>
    </figure>

    <figure style="max-width:280px;margin:0" markdown>
    ![Web dashboard: transaction list](assets/shots/web-operations.png){ loading=lazy }
    <figcaption>The transaction list with search and filters.</figcaption>
    </figure>

    </div>

=== "🧩 LM Studio"

    A local assistant answers a question about your money through MCP: the
    database does the sums, the model only retells the result. The question:
    *“How much did I spend on cafés in summer versus winter?”*

    <figure style="max-width:640px;margin:0 auto" markdown>
    ![LM Studio: the question about cafés in summer and winter and an answer with monthly totals](assets/shots/lmstudio-answer.png){ loading=lazy }
    <figcaption>LM Studio answers from your wallet data.</figcaption>
    </figure>

    How to connect it is in [“AI assistants (MCP)”](features/mcp.md). The path of
    an answer from the database to the assistant is on the
    [“How an answer gets from the database to the assistant”](components.md#mcp-answer)
    diagram.

=== "✨ Claude"

    The same question and the same answer, in Claude through the MCP connector.

    <figure style="max-width:640px;margin:0 auto" markdown>
    ![Claude: the question about cafés in summer and winter and an answer with monthly totals](assets/shots/claude-answer.png){ loading=lazy }
    <figcaption>Claude answers from the same data.</figcaption>
    </figure>

    How to connect it is in [“AI assistants (MCP)”](features/mcp.md).
