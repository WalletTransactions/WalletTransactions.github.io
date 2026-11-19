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

    ### Добавить операцию

    Сумма набирается на встроенной клавиатуре с калькулятором, затем выбираются статья и кошелёк. Кошелёк и статью можно искать по названию.

    <div style="display:flex;flex-wrap:wrap;gap:1rem;justify-content:center" markdown>

    <figure style="max-width:200px;margin:0" markdown>
    ![Новая операция: пустая форма с вводом суммы](assets/shots/android-add-empty.png){ loading=lazy }
    <figcaption>Новая операция — расход, доход или перевод.</figcaption>
    </figure>
    <figure style="max-width:200px;margin:0" markdown>
    ![Выбор статьи расхода со списком категорий](assets/shots/android-add-category.png){ loading=lazy }
    <figcaption>Статью выбирают из списка или ищут по названию.</figcaption>
    </figure>
    <figure style="max-width:200px;margin:0" markdown>
    ![Новая операция с суммой 45 €, статьёй «Продукты» и кошельком «Карта Visa»](assets/shots/android-add-filled.png){ loading=lazy }
    <figcaption>Готово — остаётся нажать «Сохранить».</figcaption>
    </figure>

    </div>

    ### Добавить операцию словами

    Если лень нажимать, напишите или продиктуйте трату — ИИ разберёт её и заполнит ту же форму. Сохраняете вы сами, ИИ в кошелёк ничего не пишет.

    <div style="display:flex;flex-wrap:wrap;gap:1rem;justify-content:center" markdown>

    <figure style="max-width:240px;margin:0" markdown>
    ![Экран «ИИ»: поле «Трата своими словами» с текстом «вчера такси 12 евро с карты Visa»](assets/shots/android-ai-input.png){ loading=lazy }
    <figcaption>Напишите, как говорите: «вчера такси 12 евро с карты Visa».</figcaption>
    </figure>
    <figure style="max-width:240px;margin:0" markdown>
    ![Форма новой операции, заполненная ИИ: расход 12 €, статья «Такси», кошелёк «Карта Visa»](assets/shots/android-ai-result.png){ loading=lazy }
    <figcaption>ИИ заполнил форму, вы проверяете и сохраняете.</figcaption>
    </figure>

    </div>

=== "🌐 Веб-кабинет"

    Веб-кабинет открывается в любом браузере без установки. На компьютере — обзор
    с динамикой по месяцам и список операций с поиском, фильтрами и итогом по выборке.

    <figure style="max-width:100%;margin:0 0 1rem" markdown>
    ![Веб-кабинет на компьютере: обзор с итогами и динамикой расходов и доходов по месяцам](assets/shots/web-wide-report.png){ loading=lazy }
    <figcaption>Обзор: расход, доход и остаток за период, динамика по месяцам.</figcaption>
    </figure>

    <figure style="max-width:100%;margin:0 0 1rem" markdown>
    ![Веб-кабинет на компьютере: список операций с фильтрами по статьям и кошелькам и итогом по выборке](assets/shots/web-wide-operations.png){ loading=lazy }
    <figcaption>Список операций: поиск, фильтры по статьям и кошелькам, итог по выборке.</figcaption>
    </figure>

    ### На телефоне

    Тот же кабинет адаптирован под телефон. Кадры сняты в мобильной ширине.

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
    на кафе за последние 12 месяцев?»*

    <figure style="max-width:640px;margin:0 auto" markdown>
    ![LM Studio: вопрос про кафе за 12 месяцев, вызов инструмента и ответ с суммой](assets/shots/lmstudio-answer.png){ loading=lazy }
    <figcaption>LM Studio вызывает инструмент и отвечает по данным кошелька.</figcaption>
    </figure>

    Как подключить — в разделе [«Подключение ИИ-ассистентов (MCP)»](features/mcp.md).

=== "✨ Claude Code"

    Ассистент отвечает на вопрос о ваших деньгах через MCP: суммы считает база, модель только пересказывает результат. Вопрос: *«Сколько я тратил на кафе за последние 12 месяцев?»*

    <figure style="max-width:640px;margin:0 auto" markdown>
    ![Claude Code: вопрос про кафе за 12 месяцев и ответ с суммами по месяцам](assets/shots/claude-answer.png){ loading=lazy }
    <figcaption>Claude Code отвечает по данным кошелька.</figcaption>
    </figure>

    Путь ответа от базы до ассистента — на схеме
    [«Как ответ доходит из базы до ассистента»](components.md#mcp-answer).

    Как подключить — в разделе [«Подключение ИИ-ассистентов (MCP)»](features/mcp.md).
