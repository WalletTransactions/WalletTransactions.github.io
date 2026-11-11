# site-build Specification

## Purpose
Сборка сайта MkDocs Material, строгая проверка и публикация в GitHub Pages.

## Requirements

### Requirement: Сборка MkDocs
Сайт SHALL собираться `mkdocs build --strict` темой Material (`language: ru`,
вкладки навигации, светлая и тёмная палитры, поиск) из `docs_dir: docs` в папку
`site/`, которая исключена из git. Зависимости — `mkdocs-material==9.5.39` и
`mkdocs-static-i18n==1.2.3` из `requirements.txt`.

#### Scenario: Локальная сборка
- **WHEN** выполнены `pip install -r requirements.txt` и `mkdocs build --strict`
- **THEN** сайт собран в `site/` без предупреждений, русская версия по адресу `/`, английская — `/en/`

#### Scenario: Битая ссылка
- **WHEN** страница ссылается на несуществующий файл или якорь
- **THEN** `mkdocs build --strict` завершается ошибкой

#### Scenario: Сборка без Python
- **WHEN** сборка запущена в контейнере `squidfunk/mkdocs-material:9.5.39` с установкой `mkdocs-static-i18n==1.2.3`
- **THEN** результат тот же, что у локальной сборки

### Requirement: Расширения Markdown
Страницы SHALL поддерживать расширения `admonition`, `attr_list`, `md_in_html`,
`tables`, `pymdownx.details`, `pymdownx.tabbed` (alternate style),
`pymdownx.superfences` с блоками `mermaid` и эмодзи Material (twemoji).

#### Scenario: Диаграмма
- **WHEN** на странице есть блок ```` ```mermaid ````
- **THEN** он отображается диаграммой (так сделана схема на странице «Из чего состоит»)

### Requirement: Публикация в GitHub Pages
Workflow `.github/workflows/pages.yml` SHALL запускаться на push в `main`, на
pull request и вручную; в задании `build` ставить Python 3.12, зависимости,
запускать `python tools/check_translations.py` и `mkdocs build --strict`.
Артефакт `site/` публикуется и разворачивается заданием `deploy` (окружение
`github-pages`) только если событие — не pull request.

#### Scenario: Pull request
- **WHEN** открыт pull request
- **THEN** выполняются проверка переводов и строгая сборка, публикации нет

#### Scenario: Push в main
- **WHEN** изменения попали в `main`
- **THEN** после успешной сборки сайт разворачивается на GitHub Pages

### Requirement: Новые задачи попадают в проект организации
Workflow `.github/workflows/add-to-project.yml` SHALL добавлять открытые,
переоткрытые и перенесённые задачи репозитория в проект организации
WalletTransactions «Wallet Tasks» секретом `ADD_TO_PROJECT_PAT`.

#### Scenario: Новая задача
- **WHEN** в репозитории открыта задача
- **THEN** она добавляется в проект https://github.com/orgs/WalletTransactions/projects/1
