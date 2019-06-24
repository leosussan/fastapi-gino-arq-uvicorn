FROM tiangolo/uvicorn-gunicorn:python3.7

RUN pip install pipenv

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN pipenv install --system --deploy --ignore-pipfile

COPY ./app /app/app