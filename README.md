# fastapi-gino-postgres
High-performance Async REST API, in Python. FastAPI + GINO + Uvicorn + PostgreSQL.

### To Use
1. Clone this Repository. `git clone https://github.com/leosussan/fastapi-gino-postgres.git`
2. Rename `.dist.env` to `.env`.
3. Run DB Migrations. 
4. Run locally with `python app/main.py`, or with the included Dockerfile / Docker-Compose file.

### Stack & Features
* **FastAPI:** touts performance on-par with NodeJS & Go + automatic Swagger + ReDoc generation. 
* **GINO:** built on SQLAlchemy core. Lightweight, simple, asynchronous ORM for PostgreSQL.
* **Uvicorn:** Lightning-fast, asynchronous ASGI server.
* **PostgreSQL:** Robust, fully-featured, scalable, open-source.
* **Optimized Dockerfile:** Optimized Dockerfile for ASGI applications, from https://github.com/tiangolo/uvicorn-gunicorn-docker.

#### Additional Libraries
* **Pydantic:** Core to FastAPI. Define how data should be in pure, canonical python; validate it with pydantic. 
* **Alembic:** Handles database migrations. Compatible with GINO.
* **SQLAlchemy_Utils:** Provides essential handles & datatypes. Compatible with GINO.
