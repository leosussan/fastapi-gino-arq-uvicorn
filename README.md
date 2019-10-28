# fastapi-gino-arq-postgres
High-performance Async REST API, in Python. FastAPI + GINO + Arq + Uvicorn (powered by Redis & PostgreSQL).

## Get Started
### Run Locally
_NOTE: You must have PostgreSQL & Redis running locally._

1. Clone this Repository. `git clone https://github.com/leosussan/fastapi-gino-arq-postgres.git`
2. Run `pipenv install --dev` from root. (Run `pip install pipenv` first, if necessary.)
3. Make a copy of `.dist.env`, rename to `.env`. Fill in PostgreSQL, Redis connection vars.
4. Generate DB Migrations: `alembic revision --autogenerate`. It will be applied when the application starts. You can trigger manually with `alembic upgrade head`.
5. Run:
    - FastAPI Application:
        * _For Active Development (w/ auto-reload):_ Run locally with `pipenv run uvicorn app.main:app --reload `
        * _For Debugging (compatible w/ debuggers, no auto-reload):_ Configure debugger to run `python app/main.py`.
    - Background Task Worker:
        * _For Active Development:_ Run with `pipenv run arq app.worker.Worker --watch ./`

### Run Locally with Docker-Compose
1. Clone this Repository. `git clone https://github.com/leosussan/fastapi-gino-arq-postgres.git`
2. Generate a DB Migration: `alembic revision --autogenerate`.*
3. Run locally using docker-compose. `docker-compose -f docker-compose.local.yml -f docker-compose.worker.yml -f docker-compose.yml up --build`.

*`app/settings/prestart.sh` will run migrations for you before the app starts.

### Build Your Application
* Create routes in `/app/routes`, import & add them to the `ROUTERS` constant in  `/app/main.py`
* Create database models to `/app/models/orm`, add them to `/app/models/orm/migrations/env.py` for migrations
* Create pydantic models in `/app/models/pydantic`
* Store complex db queries in `/app/models/orm/queries`
* Store complex tasks in `app/tasks`.
* Add / edit globals to `/.env`, expose & import them from `/app/settings/globals.py`
    * Use any coroutine as a background function: store a reference in the `ARQ_BACKGROUND_FUNCTIONS` env.
* Define code to run before launch (migrations, setup, etc) in `/app/settings/prestart.sh`

## Features
### Core Dependencies
* **FastAPI:** touts performance on-par with NodeJS & Go + automatic Swagger + ReDoc generation. 
* **GINO:** built on SQLAlchemy core. Lightweight, simple, asynchronous ORM for PostgreSQL.
* **Arq:** Asyncio + Redis = fast, resource-light job queuing & RPC.
* **Uvicorn:** Lightning-fast, asynchronous ASGI server.
* **Optimized Dockerfile:** Optimized Dockerfile for ASGI applications, from https://github.com/tiangolo/uvicorn-gunicorn-docker.

#### Additional Dependencies
* **Pydantic:** Core to FastAPI. Define how data should be in pure, canonical python; validate it with pydantic. 
* **Alembic:** Handles database migrations. Compatible with GINO.
* **SQLAlchemy_Utils:** Provides essential handles & datatypes. Compatible with GINO.
* **PostgreSQL:** Robust, fully-featured, scalable, open-source.
* **Redis:** Fast, simple, broker for the Arq task queue.
