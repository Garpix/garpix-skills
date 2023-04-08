# Garpix Skills

## Quick start

```bash
git clone https://github.com/Garpix/garpix-skills.git
cd garpix-skills
cp example.env .env
pipenv install
pipenv shell
docker-compose up -d
python3 backend/manage.py migrate
python3 backend/manage.py createsuperuser
python3 backend/manage.py runserver
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
