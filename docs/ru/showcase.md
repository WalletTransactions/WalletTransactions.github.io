# Как это выглядит

Кадры сняты на демо-данных: два кошелька и около года операций с сезонностью
расходов. Реальных сумм, имён и адресов на них нет. Где что установить —
на странице [«Где пользоваться»](platforms.md), из чего это всё состоит —
в разделе [«Из чего состоит»](components.md).

=== "📱 Android"

    Приложение работает без интернета, а синхронизация идёт в фоне. Четыре экрана
    нижней навигации:

    <div style="display:flex;flex-wrap:wrap;gap:1rem;justify-content:center" markdown>

    <figure style="max-width:240px;margin:0" markdown>
    ![Экран «Операции»: лента операций за период и карточка с итогами](assets/shots/android-operations.png){ loading=lazy }
    <figcaption>Операции — лента за период и итоги наверху.</figcaption>
    </figure>

    <figure style="max-width:240px;margin:0" markdown>
    ![Экран «Кошельки»: два кошелька с остатками](assets/shots/android-wallets.png){ loading=lazy }
    <figcaption>Кошельки — остатки по каждому счёту.</figcaption>
    </figure>

    <figure style="max-width:240px;margin:0" markdown>
    ![Экран «Отчёты»: расходы по категориям за выбранный период](assets/shots/android-reports.png){ loading=lazy }
    <figcaption>Отчёты — куда уходят деньги по категориям.</figcaption>
    </figure>

    <figure style="max-width:240px;margin:0" markdown>
    ![Экран «Ещё»: справочники и настройки](assets/shots/android-more.png){ loading=lazy }
    <figcaption>Ещё — справочники, долги, курсы и настройки.</figcaption>
    </figure>

    </div>

=== "🌐 Веб-кабинет"

    Веб-кабинет адаптирован под телефон: те же отчёты и список операций открываются
    в браузере без установки. Кадры сняты в мобильной ширине.

    <div style="display:flex;flex-wrap:wrap;gap:1rem;justify-content:center" markdown>

    <figure style="max-width:280px;margin:0" markdown>
    ![Веб-кабинет: отчёт по расходам](assets/shots/web-report.png){ loading=lazy }
    <figcaption>Отчёт по расходам за период.</figcaption>
    </figure>

    <figure style="max-width:280px;margin:0" markdown>
    ![Веб-кабинет: список операций](assets/shots/web-operations.png){ loading=lazy }
    <figcaption>Список операций с поиском и фильтрами.</figcaption>
    </figure>

    </div>

=== "🧩 LM Studio"

    Локальный ассистент отвечает на вопрос о ваших деньгах через MCP: суммы
    считает база, модель только пересказывает результат. Вопрос: *«Сколько я тратил
    на кафе летом и сколько зимой?»*

    <figure style="max-width:640px;margin:0 auto" markdown>
    ![LM Studio: вопрос про кафе летом и зимой и ответ с суммами по месяцам](assets/shots/lmstudio-answer.png){ loading=lazy }
    <figcaption>LM Studio отвечает по данным кошелька.</figcaption>
    </figure>

    Как подключить — в разделе [«Подключение ИИ-ассистентов (MCP)»](features/mcp.md).
    Путь ответа от базы до ассистента — на схеме
    [«Как ответ доходит из базы до ассистента»](components.md#mcp-answer).

=== "✨ Claude"

    Тот же вопрос, тот же ответ — в Claude через коннектор MCP.

    <figure style="max-width:640px;margin:0 auto" markdown>
    ![Claude: вопрос про кафе летом и зимой и ответ с суммами по месяцам](assets/shots/claude-answer.png){ loading=lazy }
    <figcaption>Claude отвечает по тем же данным.</figcaption>
    </figure>

    Как подключить — в разделе [«Подключение ИИ-ассистентов (MCP)»](features/mcp.md).
