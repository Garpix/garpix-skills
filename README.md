# Garpix Skills

## Quick start

Apply environment variables:

```
cp example.env .env
```

Install python dependencies

```
make venv
```

Run the project

```
make install
```

## Frontend

### Dev

Install frontend dependencies

```bash
cd frontend/app
yarn
```

Development start

```bash
yarn dev
```

### Production (CI/CD)

Production start/

Change environment variables `DEBUG_FRONTEND=False`

```bash
cd frontend/app
yarn install --frozen-lockfile
yarn build
```