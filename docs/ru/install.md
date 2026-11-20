# Установка сервера дома

Пошаговая инструкция: от пустого Linux-компьютера до работающего веб-кабинета,
к которому подключается телефон. Идём **от минимума к максимуму** — после
каждого шага у вас есть рабочий результат, и остановиться можно на любом.

!!! info "Комплект «одной командой» — в разработке"
    Эта инструкция — ручная установка по шагам. Готовый комплект, который
    поднимает всё одной командой, пока [в разработке](roadmap.md).

| Шаг | Что получаете |
|---|---|
| [1. Минимум](#minimum) | Веб-кабинет, синхронизация с телефоном, отчёты, Telegram-бот |
| [2. ИИ](#ai) | Траты своими словами, импорт выписок, вопросы о деньгах |
| [3. Доступ для ИИ-ассистентов](#mcp) | Подключение внешних ассистентов по MCP |
| [4. Резервные копии](#backup) | Ежедневные копии базы на отдельный диск |
| [5. Графики и журнал событий](#diagnostics) | Разбор проблем, если что-то пошло не так |
| [6. Телефон](#phone) | Android-приложение работает с вашим сервером |

## Что понадобится { #requirements }

- Компьютер с **Linux**, который может быть включён постоянно, и 4 ГБ памяти
  (подробнее — в разделе [«Свой сервер дома»](self-hosting.md#diagnostics)).
- **Docker** с плагином `docker compose` версии 2, а также `git`, `curl` и
  `openssl`.
- Аккаунт **Google** — вход в кабинет идёт только через него.
- Для ИИ — видеокарта с 8 ГБ памяти (шаг 2). Без неё сервер полностью
  работает, функции ИИ просто не показываются.

!!! warning "Доступ к образам"
    Образы сервера и репозиторий с описанием стека сейчас лежат в закрытом
    реестре GitHub. Для установки нужен доступ к организации
    [WalletTransactions](https://github.com/WalletTransactions) и токен GitHub
    с правом `read:packages`.

## Шаг 1. Минимум { #minimum }

Поднимаются база, сервисы входа, учёта, отчётов, ИИ-шлюз, бот и веб-кабинет.
Снаружи открыт один порт — **8090** (единая точка входа).

### 1.1. Подготовка

Репозитории лежат **рядом**, имена папок совпадают с именами репозиториев:

```text
WalletTransactions/
├── wallet-infra/
├── google-auth/   wallet-api/   wallet-report/
├── wallet-ai/     wallet-gateway/   wallet-telegram/
```

```bash
mkdir WalletTransactions && cd WalletTransactions
for r in wallet-infra google-auth wallet-api wallet-report wallet-ai wallet-gateway wallet-telegram; do
    git clone git@github.com:WalletTransactions/$r.git
done
docker login ghcr.io        # логин GitHub и токен с правом read:packages
```

Собирать ничего не нужно: готовые образы скачиваются из реестра.

### 1.2. Вход через Google

В [Google Cloud Console](https://console.cloud.google.com/) создайте
**OAuth client ID** типа *Web application*. Запишите `Client ID` и
`Client secret`. В *Authorized redirect URIs* добавьте:

```text
http://localhost:8090/auth/google/callback
```

Если хотите заходить с других устройств дома, добавьте ещё адрес вида
`http://192.168.1.50.nip.io:8090/auth/google/callback` (ваш домашний IP вместо
`192.168.1.50`): Google не принимает голый IP-адрес, а `nip.io` превращает его
в обычное доменное имя.

### 1.3. Telegram-бот

В Telegram откройте [@BotFather](https://t.me/BotFather), создайте бота и
сохраните его **токен** и **имя** (без `@`). Пользоваться ботом необязательно,
но его настройки нужны серверу, чтобы стартовать.

### 1.4. Секреты

Все пароли лежат вне репозитория — в `~/.config/wallet-secrets/prod/`.
Права строгие, сервер не стартует с другими: каталог **700**, файлы `.env`
**600**, ключ `.pem` **644**.

```bash
cd wallet-infra
S=~/.config/wallet-secrets/prod
install -m 700 -d "$S"
install -m 600 infra/db/.env.example "$S/db.env"
for s in google-auth wallet-api wallet-report wallet-ai wallet-gateway wallet-telegram; do
    install -m 600 "../$s/.env.example" "$S/$s.env"
done
openssl genrsa -out "$S/jwt_signing_key.pem" 2048 && chmod 644 "$S/jwt_signing_key.pem"
```

Теперь откройте файлы и впишите значения:

| Файл | Что вписать |
|---|---|
| `db.env` | Замените **все** `change-me-…` на разные пароли: `openssl rand -hex 24`. Допустимы только латиница, цифры и `. _ ~ -` |
| `google-auth.env` | `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`; `REDIRECT_URL=http://localhost:8090/auth/google/callback`; `ADMIN_EMAILS` — ваш адрес Google (первый вход создаст администратора); `TELEGRAM_SERVICE_SECRET` — любая случайная строка; `TELEGRAM_BOT_USERNAME`; `JWT_RSA_PRIVATE_KEY_PATH=/app/jwt_signing_key.pem` |
| `wallet-telegram.env` | `TELEGRAM_BOT_TOKEN`, `TELEGRAM_BOT_USERNAME` и **тот же** `TELEGRAM_SERVICE_SECRET`, что в `google-auth.env` |

Остальные адреса и порты в файлах менять не нужно: они переопределяются
настройками стека.

!!! danger "Пароли хранят ваши деньги"
    `db.env` и `jwt_signing_key.pem` не кладите в облако и не отправляйте в
    мессенджеры, а копию храните отдельно от самих данных.

### 1.5. Версии образов

Создайте файл с версиями. Номера возьмите из раздела *Packages* организации
на GitHub — берите **последние финальные** (вида `1.2.3`, без `-rc`):

```bash
mkdir -p ~/.local/state/wallet-envs/prod
cat > ~/.local/state/wallet-envs/prod/tags.env <<'EOF'
GOOGLE_AUTH_TAG=<версия>
WALLET_API_TAG=<версия>
WALLET_REPORT_TAG=<версия>
WALLET_AI_TAG=<версия>
WALLET_GATEWAY_TAG=<версия>
WALLET_WEB_TAG=<версия>
WALLET_TELEGRAM_TAG=<версия>
WALLET_MCP_TAG=<версия>
EOF
```

Пропущенная строка — и запуск остановится с понятным сообщением, ничего не
создав.

### 1.6. Запуск

В настройках контура (`infra/env/prod.env`) ИИ по умолчанию смотрит на
локальную модель. Если видеокарты нет, оставьте `LLM_URL=` пустым. Затем:

```bash
bash infra/env/up.sh prod
curl -s http://localhost:8090/healthz
```

Скрипт сам создаёт сеть, поднимает базу, накатывает схему и запускает
сервисы, дожидаясь, пока каждый ответит. Повторный запуск безопасен.

### 1.7. Первый вход

Откройте `http://localhost:8090` и войдите через Google адресом из
`ADMIN_EMAILS` — вы администратор. Данных пока нет, есть только пустая схема.
В кабинете нажмите «Подключить Telegram» — бот ответит.

## Шаг 2. ИИ на своей видеокарте { #ai }

Нужна видеокарта с 8 ГБ памяти (проверено на GTX 1070; модели до 8B в
квантовании Q4).

1. Установите [LM Studio](https://lmstudio.ai) и его консольную утилиту `lms`.
2. Запустите сервер и загрузите модель под именем `wallet-parse`:
   `bash wallet-ai/scripts/lms-load.sh` (скачайте и репозиторий `wallet-ai`,
   если ещё не клонировали). Скрипт безопасно запускать повторно; после
   перезагрузки компьютера запустите его снова.
3. В настройках сервера LM Studio включите **«Serve on Local Network»** и
   токен API. Порт `1234` откройте в файрволе только для Docker-сетей.
4. Впишите токен в `~/.config/wallet-secrets/prod/wallet-ai.env`
   (`LLM_API_KEY=…`) и перезапустите: `bash infra/env/up.sh prod`.

Проверка: в кабинете появились функции ИИ. Подробный журнал запросов в
LM Studio **выключите** — в нём тексты ваших трат.

## Шаг 3. Доступ для ИИ-ассистентов { #mcp }

Сервер уже умеет отвечать внешним ассистентам по MCP (токен выпускается в
кабинете). Чтобы чат в приложении тоже мог читать ваши данные, включите
обмен токенов — три строки с двумя случайными секретами
(`openssl rand -hex 32`):

| Файл | Строка |
|---|---|
| `google-auth.env` | `TOKEN_EXCHANGE_SECRETS=wallet-ai=<A>,wallet-mcp=<M>` |
| `wallet-mcp.env` (права 600) | `AUTH_EXCHANGE_SECRET=<M>` |
| `wallet-ai.env` | `AUTH_EXCHANGE_SECRET=<A>` |

Затем `bash infra/env/up.sh prod`. Адрес для ассистента:
`http://<адрес сервера>:8090/api/mcp/` — **слэш в конце обязателен**.

## Шаг 4. Резервные копии { #backup }

Сервер хранит данные в томе Docker. Копии нужны на **другом физическом диске**
— копия рядом с базой не спасёт при отказе диска.

```bash
export WALLET_BACKUP_DIR=/mnt/backup/wallet
bash infra/env/backup.sh prod --label manual
```

Скрипт делает дамп каждой базы и проверяет, что он читается. Чтобы копии
шли каждую ночь, добавьте команду в `cron`.

Восстановление:

```bash
docker exec -i wallet-prod-db-1 sh -c \
    'pg_restore -U "$POSTGRES_USER" -d wallet_api --clean --if-exists' \
    < "$WALLET_BACKUP_DIR/prod/wallet/<файл>.dump"
```

## Шаг 5. Графики и журнал событий { #diagnostics }

Оба набора необязательны и после перезагрузки сами не включаются:

```bash
bash infra/monitoring/up.sh                              # графики: http://localhost:13000
docker compose -f infra/logging/compose.yaml up -d       # журнал: http://localhost:15601
```

В графики входите как `admin`; пароль лежит в
`~/.config/wallet-secrets/monitoring.env`. Журнал занимает около 1.5 ГБ памяти и
не рассчитан на доступ из сети — не открывайте его наружу.

Без них логи не теряются: `journalctl CONTAINER_NAME=wallet-prod-wallet-api-1`.

## Шаг 6. Телефон { #phone }

1. Установите Android-приложение.
2. «Ещё» → «Интеграции» → введите адрес сервера: `http://<IP компьютера>:8090/`.
3. Войдите через Google. Синхронизация идёт в фоне, как только телефон оказался
   дома. Вне дома он работает офлайн и догоняет по возвращении.

## Обновление

Новые версии — новые номера в `tags.env`. Перед обновлением сделайте копию
(шаг 4), потом:

```bash
# в ~/.local/state/wallet-envs/prod/tags.env поменяйте нужные версии
bash infra/env/up.sh prod
```

Скрипт накатит миграции схемы и пересоздаст только изменившиеся сервисы. Если
что-то пошло не так, верните прежние номера версий и запустите его снова.

## Если не получается { #troubleshooting }

| Что происходит | Что делать |
|---|---|
| `docker compose up` падает на «не задана переменная» | Запускайте только `bash infra/env/up.sh prod` — голый compose так и задуман не работать |
| «права … нужно 600» | `chmod 700` на каталог секретов, `600` на файлы `.env`, `644` на `.pem` |
| Сервер падает после правки паролей | В `db.env` попал символ вне `A-Za-z0-9._~-` (например, кириллица) |
| Google: `redirect_uri_mismatch` | Адрес в `REDIRECT_URL` должен совпасть **символ в символ** с записью в Google Cloud Console |
| Бот не отвечает, в логах 409 | Один токен — один процесс; не запускайте второй экземпляр с тем же ботом |
| Ассистент получает 401 | Проверьте слэш в конце: `/api/mcp/` |
| Пароли в `db.env` поменяли, а база не приняла | Роли создаются при первом старте пустой базы; пароль меняйте и в самой базе |
