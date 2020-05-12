FROM tiangolo/uvicorn-gunicorn:python3.8-alpine3.10

RUN apk update && apk add gcc libffi-dev g++ postgresql-dev make curl

RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python

COPY pyproject.toml pyproject.toml
COPY poetry.lock poetry.lock

RUN poetry config virtualenvs.create false && poetry install --no-dev --no-ansi

RUN apk del libffi-dev g++ make curl

COPY ./app /app/app

COPY ./alembic.ini /app/alembic.ini

COPY ./app/settings/prestart.sh /app/prestart.sh
