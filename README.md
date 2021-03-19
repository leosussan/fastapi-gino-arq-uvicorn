# fastapi-gino-arq-uvicorn
High-performance Async REST API, in Python. FastAPI + GINO + Arq + Uvicorn (powered by Redis & PostgreSQL).

## Contents
- [fastapi-gino-arq-uvicorn](#fastapi-gino-arq-uvicorn)
  - [Contents](#contents)
  - [Get Started](#get-started)
    - [Setup](#setup)
    - [Run](#run)
      - [Run Locally](#run-locally)
      - [Run Locally with Docker-Compose.](#run-locally-with-docker-compose)
    - [Build Your Application](#build-your-application)
  - [Features](#features)
    - [Core Dependencies](#core-dependencies)
      - [Additional Dependencies](#additional-dependencies)

## Get Started
### Setup
1. Clone this Repository. `git clone https://github.com/leosussan/fastapi-gino-arq-uvicorn.git`
2. Install `Python 3.8` and `poetry`.
    * Recommended Method: `asdf` - a universal version manager (think `nvm` or `pyenv`)
        * Follow [these instructions](https://asdf-vm.com/#/core-manage-asdf-vm?id=install-asdf-vm) to install `asdf`.
        * Run the following commands from the project root:
            * `asdf plugin add python`
            * `asdf plugin add poetry`
            * `asdf install` -- will download & configure this project's `Python` + `poetry` setup
        * _~NOTE_: your machine must have a system version of Python installed. If you don't, run the following: `asdf install python 3.8.2 && asdf global python 3.8.2`
    * If you have `Python 3.8` and `poetry` installed already, please feel free to skip.
3. Install dependencies (`poetry install`).
4. Activate pre-commit hooks (in `poetry shell`, run `pre-commit install`).
5. Make a copy of `.dist.env`, rename to `.env`. Fill in PostgreSQL, Redis, Sentry (optional) variables.
6. Generate DB Migrations: in `poetry shell`, run `alembic revision --autogenerate`. 
    * Apply migrations manually with `alembic upgrade head`.
    * If using the Dockerfile, migrations are applied at startup.

### Run

#### Run Locally
_NOTE: You must have PostgreSQL & Redis running locally._

1. Make sure PostgreSQL & Redis are running locally.
2. Run:
    - FastAPI Application:
        * _For Active Development (w/ auto-reload):_ Run locally with `poetry run task app`
        * _For Debugging (compatible w/ debuggers, no auto-reload):_ Configure debugger to run `python app/main.py`.
    - Background Task Worker:
        * _For Active Development:_ Run  `poetry run task worker`

#### Run Locally with Docker-Compose.
1. Make sure `Docker` is running locally.
2. Run `poetry run task compose-up`*.
   - Run `poetry run task compose-down` to spin down, clean up.

*`app/settings/prestart.sh` will run migrations for you before the app starts.

### Build Your Application
* Create routes in `/app/routes`, import & add them to the `ROUTERS` constant in  `/app/main.py`
* Create database models to `/app/models/orm`, add them to `/app/models/orm/migrations/env.py` for migrations
* Create pydantic models in `/app/models/pydantic`
* Store complex db queries in `/app/models/orm/queries`
* Store complex tasks in `app/tasks`.
* Add / edit globals to `/.env`, expose & import them from `/app/settings/globals.py`
    * Use any coroutine as a background function: store a reference in the `ARQ_BACKGROUND_FUNCTIONS` env.
    * Set `SENTRY_DSN` in your environment to enable Sentry.
* Define code to run before launch (migrations, setup, etc) in `/app/settings/prestart.sh`

## Features
### Core Dependencies
* **FastAPI:** touts performance on-par with NodeJS & Go + automatic Swagger + ReDoc generation. 
* **GINO:** built on SQLAlchemy core. Lightweight, simple, asynchronous ORM for PostgreSQL.
* **Arq:** Asyncio + Redis = fast, resource-light job queuing & RPC.
* **Uvicorn:** Lightning-fast, asynchronous ASGI server.
* **Optimized Dockerfile:** Optimized Dockerfile for ASGI applications, from https://github.com/tiangolo/uvicorn-gunicorn-docker.

#### Additional Dependencies
* **PostgreSQL:** Robust, fully-featured, scalable, open-source.
* **Redis:** Fast, simple, broker for the Arq task queue.
* **Pydantic:** Core to FastAPI. Define how data should be in pure, canonical python; validate it with pydantic. 
* **Alembic:** Handles database migrations. Compatible with GINO.
* **SQLAlchemy_Utils:** Provides essential handles & datatypes. Compatible with GINO.
* **Sentry:** Open-source, cloud-hosted error + event monitoring.
* **Pre-Commit:** automatic formatting (`black` + `isort`) and linting (`flake8`).
* **Taskipy:** Small, flexible task runner for Poetry.
