# Installing the server at home

A step-by-step guide: from an empty Linux computer to a working web
dashboard your phone connects to. We go **from the minimum to the maximum** —
after every step you have something working, and you can stop at any of them.

!!! info "A one-command kit is in development"
    This guide is a manual, step-by-step installation. A ready-made kit that
    brings everything up with one command is [in development](roadmap.md).

| Step | What you get |
|---|---|
| [1. Minimum](#minimum) | Web dashboard, phone sync, reports, Telegram bot |
| [2. AI](#ai) | Expenses in plain words, statement import, questions about money |
| [3. Access for AI assistants](#mcp) | Connecting external assistants over MCP |
| [4. Backups](#backup) | Database copies on a separate disk |
| [5. Charts and event log](#diagnostics) | Troubleshooting when something goes wrong |
| [6. Phone](#phone) | The Android app works with your server |

## What you need { #requirements }

- A **Linux** computer that can stay on, with 4 GB of memory (details in
  ["Your own server at home"](self-hosting.md#diagnostics)).
- **Docker** with the `docker compose` v2 plugin, plus `git`, `curl` and
  `openssl`.
- A **Google** account — sign-in to the dashboard goes only through it.
- For AI, a graphics card with 8 GB of memory (step 2). Without it the server
  works fully; AI features are simply hidden.

!!! warning "Access to the images"
    The server images and the repository describing the stack are currently in
    a private GitHub registry. You need access to the
    [WalletTransactions](https://github.com/WalletTransactions) organization
    and a GitHub token with the `read:packages` permission.

## Step 1. The minimum { #minimum }

This brings up the database, the sign-in, ledger, reports and AI gateway
services, the bot and the web dashboard. One port is open to the outside —
**8090** (the single entry point).

### 1.1. Preparation

Repositories sit **side by side**; folder names match repository names:

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
docker login ghcr.io        # your GitHub login and a token with read:packages
```

Nothing is built: ready images are pulled from the registry.

### 1.2. Google sign-in

In the [Google Cloud Console](https://console.cloud.google.com/) create an
**OAuth client ID** of type *Web application*. Note the `Client ID` and
`Client secret`. Under *Authorized redirect URIs* add:

```text
http://localhost:8090/auth/google/callback
```

To sign in from other devices at home, also add an address like
`http://192.168.1.50.nip.io:8090/auth/google/callback` (your home IP instead of
`192.168.1.50`): Google does not accept a bare IP address, and `nip.io` turns
it into an ordinary domain name.

### 1.3. Telegram bot

In Telegram open [@BotFather](https://t.me/BotFather), create a bot and save
its **token** and **username** (without `@`). You do not have to use the bot,
but the server needs its settings to start.

### 1.4. Secrets

All passwords live outside the repository, in `~/.config/wallet-secrets/prod/`.
Permissions are strict and the server will not start with others: the folder
**700**, `.env` files **600**, the `.pem` key **644**.

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

Now open the files and fill in the values:

| File | What to enter |
|---|---|
| `db.env` | Replace **every** `change-me-…` with a different password: `openssl rand -hex 24`. Only Latin letters, digits and `. _ ~ -` are allowed |
| `google-auth.env` | `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`; `REDIRECT_URL=http://localhost:8090/auth/google/callback`; `ADMIN_EMAILS` — your Google address (the first sign-in creates the administrator); `TELEGRAM_SERVICE_SECRET` — any random string; `TELEGRAM_BOT_USERNAME`; `JWT_RSA_PRIVATE_KEY_PATH=/app/jwt_signing_key.pem` |
| `wallet-telegram.env` | `TELEGRAM_BOT_TOKEN`, `TELEGRAM_BOT_USERNAME` and the **same** `TELEGRAM_SERVICE_SECRET` as in `google-auth.env` |

Other addresses and ports in the files need no change: the stack settings
override them.

!!! danger "These passwords guard your money"
    Do not put `db.env` or `jwt_signing_key.pem` in the cloud or send them in
    messengers, and keep backups apart from the data itself.

### 1.5. Image versions

Create the file with versions. Take the numbers from the organization's
*Packages* section on GitHub — use the **latest final** ones (like `1.2.3`,
without `-rc`):

```bash
mkdir -p ~/.local/state/wallet-envs/prod
cat > ~/.local/state/wallet-envs/prod/tags.env <<'EOF'
GOOGLE_AUTH_TAG=<version>
WALLET_API_TAG=<version>
WALLET_REPORT_TAG=<version>
WALLET_AI_TAG=<version>
WALLET_GATEWAY_TAG=<version>
WALLET_WEB_TAG=<version>
WALLET_TELEGRAM_TAG=<version>
WALLET_MCP_TAG=<version>
EOF
```

A missing line makes the start stop with a clear message, creating nothing.

### 1.6. Start

In the environment settings (`infra/env/prod.env`) AI points to a local model
by default. With no graphics card, leave `LLM_URL=` empty. Then:

```bash
bash infra/env/up.sh prod
curl -s http://localhost:8090/healthz
```

The script creates the network, starts the database, applies the schema and
starts the services, waiting until each one answers. Running it again is safe.

### 1.7. First sign-in

Open `http://localhost:8090` and sign in with Google using the address from
`ADMIN_EMAILS` — you are the administrator. There is no data yet, only an
empty schema. In the dashboard press "Connect Telegram" — the bot replies.

## Step 2. AI on your own graphics card { #ai }

You need a graphics card with 8 GB of memory (tested on a GTX 1070; models up
to 8B quantized to Q4).

1. Install [LM Studio](https://lmstudio.ai) and its command-line tool `lms`.
2. Start the server and load the model under the name `wallet-parse`:
   `bash wallet-ai/scripts/lms-load.sh` (clone the `wallet-ai` repository too,
   if you have not). The script is safe to run again; run it again after the
   computer reboots.
3. In the LM Studio server settings turn on **"Serve on Local Network"** and
   an API token. Open port `1234` in the firewall for Docker networks only.
4. Put the token into `~/.config/wallet-secrets/prod/wallet-ai.env`
   (`LLM_API_KEY=…`) and restart: `bash infra/env/up.sh prod`.

Check: AI features show up in the dashboard. **Turn off** verbose request
logging in LM Studio — it contains the texts of your expenses.

## Step 3. Access for AI assistants { #mcp }

The server can already answer external assistants over MCP (the token is
issued in the dashboard). For the in-app chat to read your data too, turn on
token exchange — three lines with two random secrets (`openssl rand -hex 32`):

| File | Line |
|---|---|
| `google-auth.env` | `TOKEN_EXCHANGE_SECRETS=wallet-ai=<A>,wallet-mcp=<M>` |
| `wallet-mcp.env` (permissions 600) | `AUTH_EXCHANGE_SECRET=<M>` |
| `wallet-ai.env` | `AUTH_EXCHANGE_SECRET=<A>` |

Then `bash infra/env/up.sh prod`. The address for an assistant is
`http://<server address>:8090/api/mcp/` — **the trailing slash is required**.

## Step 4. Backups { #backup }

The server keeps data in a Docker volume. Copies belong on a **different
physical disk** — a copy next to the database will not survive a disk failure.

```bash
export WALLET_BACKUP_DIR=/mnt/backup/wallet
bash infra/env/backup.sh prod --label manual
```

The script dumps every database and checks that the dump is readable. For
nightly copies, put the command in `cron`.

Restore:

```bash
docker exec -i wallet-prod-db-1 sh -c \
    'pg_restore -U "$POSTGRES_USER" -d wallet_api --clean --if-exists' \
    < "$WALLET_BACKUP_DIR/prod/wallet/<file>.dump"
```

## Step 5. Charts and event log { #diagnostics }

Both sets are optional and do not start by themselves after a reboot:

```bash
bash infra/monitoring/up.sh                              # charts: http://localhost:13000
docker compose -f infra/logging/compose.yaml up -d       # log: http://localhost:15601
```

Sign in to the charts as `admin`; the password is in
`~/.config/wallet-secrets/monitoring.env`. The event log takes about 1.5 GB of
memory and is not meant to be reached over the network — do not expose it.

Without them logs are not lost:
`journalctl CONTAINER_NAME=wallet-prod-wallet-api-1`.

## Step 6. Phone { #phone }

1. Install the Android app.
2. "More" → "Integrations" → enter the server address:
   `http://<computer IP>:8090/`.
3. Sign in with Google. Sync runs in the background as soon as the phone is at
   home. Away from home it works offline and catches up on return.

## Updating

New versions mean new numbers in `tags.env`. Make a backup first (step 4),
then:

```bash
# edit the versions you need in ~/.local/state/wallet-envs/prod/tags.env
bash infra/env/up.sh prod
```

The script applies schema migrations and recreates only the changed services.
If something goes wrong, put the previous version numbers back and run it
again.

## If it does not work { #troubleshooting }

| What happens | What to do |
|---|---|
| `docker compose up` fails on "variable is not set" | Run only `bash infra/env/up.sh prod` — bare compose is designed not to work |
| "permissions … need 600" | `chmod 700` on the secrets folder, `600` on `.env` files, `644` on the `.pem` |
| The server fails after editing passwords | `db.env` has a character outside `A-Za-z0-9._~-` (for example, Cyrillic) |
| Google: `redirect_uri_mismatch` | `REDIRECT_URL` must match the entry in Google Cloud Console **character for character** |
| The bot is silent, logs show 409 | One token, one process; do not run a second instance of the same bot |
| An assistant gets 401 | Check the trailing slash: `/api/mcp/` |
| Changed passwords in `db.env`, the database refused | Roles are created on the first start of an empty database; change the password in the database too |
