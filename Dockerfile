FROM tiangolo/uvicorn-gunicorn:python3.7-alpine3.8

RUN pip install pipenv

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN apk update && apk add gcc libffi-dev g++ postgresql-dev

RUN pipenv install --system --deploy --ignore-pipfile

RUN apk del libffi-dev g++

COPY ./app /app/app

COPY ./alembic.ini /app/alembic.ini

COPY ./app/settings/prestart.sh /app/prestart.sh
