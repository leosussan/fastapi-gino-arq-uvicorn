# fastapi-gino-postgres
High-performance Async REST API, in Python. FastAPI + GINO + Uvicorn + PostgreSQL.

## Get Started
### Quickstart
1. Clone this Repository. `git clone https://github.com/leosussan/fastapi-gino-postgres.git`
2. Rename `.dist.env` to `.env`, fill in PostgreSQL connection vars.
3. Run DB Migrations: `alembic revision --autogenerate && alembic upgrade head
`.
4. Run locally with `python app/main.py`, or with the included Dockerfile / Docker-Compose file.

### Build Your Application
* Create routes in `./app/routes`, import & add them to the `ROUTERS` constant in  `./app/main.py`.
* Create database models to `./app/models/orm`, add them to `./app/models/orm/migrations/env.py` for migrations.
* Create pydantic models in `./app/models/pydantic`
* Store complex db queries in `./app/models/orm/queries`
* Add / edit globals to `./.env`, expose & import them from `./app/settings/globals.py`

## Features
### Core Dependencies
* **FastAPI:** touts performance on-par with NodeJS & Go + automatic Swagger + ReDoc generation. 
* **GINO:** built on SQLAlchemy core. Lightweight, simple, asynchronous ORM for PostgreSQL.
* **Uvicorn:** Lightning-fast, asynchronous ASGI server.
* **PostgreSQL:** Robust, fully-featured, scalable, open-source.
* **Optimized Dockerfile:** Optimized Dockerfile for ASGI applications, from https://github.com/tiangolo/uvicorn-gunicorn-docker.

#### Additional Dependencies
* **Pydantic:** Core to FastAPI. Define how data should be in pure, canonical python; validate it with pydantic. 
* **Alembic:** Handles database migrations. Compatible with GINO.
* **SQLAlchemy_Utils:** Provides essential handles & datatypes. Compatible with GINO.
