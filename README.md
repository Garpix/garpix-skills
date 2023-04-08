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

## Local dev

```bash
cp example.env .env
sed -i -e 's/POSTGRES_HOST=localhost/POSTGRES_HOST=postgres/g' .env
sed -i -e 's/REDIS_HOST=localhost/REDIS_HOST=redis/g' .env
docker-compose -f docker-compose-local.yml up -d
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
## Quick deployment

```bash
cp example.env .env
# change variables
docker-compose -f docker-compose-production.yml build
docker-compose -f docker-compose-production.yml up -d
```

### Dump neo4j database

```bash
docker-compose down
docker-compose run neo4j bash -c "neo4j-admin database dump neo4j --to-stdout --overwrite-destination=true > /dumps/neo4j_$(date '+%Y-%m-%d').dump"
```

### Restore neo4j database

```bash
docker-compose down
docker-compose run neo4j bash -c "neo4j-admin database load neo4j --from-stdin --overwrite-destination=true < /dumps/neo4j.dump"
```
