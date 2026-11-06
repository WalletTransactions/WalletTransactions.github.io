# wallet-site

Сайт продукта «Посчитай и сбереги» (Count & Save): описание, бизнес-сервисы,
возможности, состав, планы. Позже — руководство пользователя и политика
конфиденциальности.

Собирается [MkDocs Material](https://squidfunk.github.io/mkdocs-material/)
с плагином [mkdocs-static-i18n](https://ultrabug.github.io/mkdocs-static-i18n/),
публикуется в GitHub Pages workflow-ом `.github/workflows/pages.yml`.

```bash
pip install -r requirements.txt
mkdocs serve                        # http://127.0.0.1:8000 (ru), /en/ (en)
mkdocs build --strict               # проверка ссылок, результат в site/
python tools/check_translations.py  # каких страниц не хватает в переводах
```

Без Python, в Docker:

```bash
docker run --rm -v "$PWD":/docs --entrypoint sh squidfunk/mkdocs-material:9.5.39 \
  -c "pip install -q mkdocs-static-i18n==1.2.3 && mkdocs build --strict"
```

## Структура

| Путь | Что |
|---|---|
| `docs/ru/` | Русский — язык по умолчанию, адрес `/` |
| `docs/en/` | Английский, адрес `/en/` |
| `docs/<lang>/index.md` | Главная: о продукте, для кого |
| `docs/<lang>/services.md` | Матрица бизнес-сервисов × клиентов |
| `docs/<lang>/features/` | Страница на каждый сервис |
| `docs/<lang>/components.md` | Из чего состоит (без внутренних деталей) |
| `docs/<lang>/roadmap.md` | Что в разработке |
| `tools/check_translations.py` | Сверка переводов с `docs/ru/` |

## Локализация

- Одна папка на язык, **имена файлов во всех папках одинаковые**:
  `docs/ru/features/ai.md` ↔ `docs/en/features/ai.md`. Так переключатель
  языка ведёт на ту же страницу.
- Меню (`nav` в `mkdocs.yml`) одно на все языки и пишется по-русски;
  заголовки переводятся в `nav_translations` у каждого языка.
- Нет перевода страницы — показывается русская версия (`fallback_to_default`).
  Пропуски выводит `tools/check_translations.py`, в CI — как предупреждения.
- Якоря внутри страниц задаются явно и латиницей
  (`## Заголовок { #statement-import }`), одинаково во всех языках.
  Автоматические кириллические якоря MkDocs выбрасывает.
- Сначала правится русская страница, потом переводы.

### Как добавить язык

1. Скопировать `docs/en/` в `docs/<locale>/` (например, `de`, `es`, `uk`) и
   перевести страницы. Всё непереведённое удалить: вместо него покажется
   русская версия.
2. Добавить язык в `plugins.i18n.languages` в `mkdocs.yml` по образцу `en`:
   `locale`, `name` (самоназвание языка), `build: true`, `site_name`,
   `site_description`, `theme.palette` с переведёнными подписями
   переключателя темы и `nav_translations` для всех пунктов меню.
3. Проверить: `mkdocs build --strict` и `python tools/check_translations.py --strict`.

## Правила для текстов

Источник фактов — OpenSpec-спеки репозиториев (`*/openspec/specs`) и
`.github-private/profile/README.md`. Сайт публичный: портов, имён внутренних
ручек, токенов и адресов контуров здесь быть не должно.

> GitHub Pages на бесплатном плане работает только из публичного
> репозитория.
