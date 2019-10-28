import sys

sys.path.extend(["./"])

from sentry_sdk.integrations.asgi import SentryAsgiMiddleware

from app.application import app
from app.routes.users import router as user_router
from app.settings.globals import SENTRY_DSN


ROUTERS = (user_router,)

for r in ROUTERS:
    app.include_router(r)

if SENTRY_DSN not in (None, "", " "):
    app.add_middleware(SentryAsgiMiddleware)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8888, log_level="info")
