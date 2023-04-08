FROM node:16-alpine as builder

COPY frontend/app /code/frontend/app/

WORKDIR /code/frontend/app

RUN yarn install --frozen-lockfile
RUN yarn build

FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1

RUN apt update && apt install git libxml2 libxml2-dev libxslt-dev gcc python3-dev musl-dev -y

RUN mkdir -p /code && \
    mkdir -p /code/public/static && \
    mkdir -p /code/public/media

COPY Pipfile Pipfile.lock /code/

COPY frontend /code/frontend/
COPY --from=builder /code/frontend/static/build /code/frontend/static/build/
COPY backend /code/backend/

WORKDIR /code

RUN pip3 install pipenv
COPY Pipfile Pipfile.lock /code/
RUN pipenv sync --system

COPY ./run.sh /code/
COPY ./run_local.sh /code/
COPY ./uwsgi.ini /code/

RUN mkdir -p /var/log/uwsgi/

WORKDIR /code/backend/

EXPOSE 8080
