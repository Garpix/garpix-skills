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
