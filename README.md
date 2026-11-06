# wallet-site

Сайт продукта «Посчитай и сбереги»: описание, бизнес-сервисы, возможности,
состав, планы. Позже — руководство пользователя и политика конфиденциальности.

Собирается [MkDocs Material](https://squidfunk.github.io/mkdocs-material/),
публикуется в GitHub Pages workflow-ом `.github/workflows/pages.yml`.

```bash
pip install -r requirements.txt
mkdocs serve          # http://127.0.0.1:8000
mkdocs build --strict # проверка ссылок, результат в site/
```

| Путь | Что |
|---|---|
| `docs/index.md` | Главная: о продукте, для кого |
| `docs/services.md` | Матрица бизнес-сервисов × клиентов |
| `docs/features/` | Страница на каждый сервис |
| `docs/components.md` | Из чего состоит (без внутренних деталей) |
| `docs/roadmap.md` | Что в разработке |

Источник фактов — OpenSpec-спеки репозиториев (`*/openspec/specs`) и
`.github-private/profile/README.md`. Сайт публичный: портов, имён
внутренних ручек, токенов и адресов контуров здесь быть не должно.

> GitHub Pages на бесплатном плане работает только из публичного
> репозитория.
