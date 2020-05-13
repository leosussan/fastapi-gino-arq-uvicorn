# isort:skip_file

import sys

sys.path.extend(["./"])

from sentry_sdk.integrations.asgi import SentryAsgiMiddleware
from starlette.datastructures import Secret

from app.application import app
from app.routes.users import router as user_router
from app.settings.globals import SENTRY_DSN


ROUTERS = (user_router,)

for r in ROUTERS:
    app.include_router(r)

if isinstance(SENTRY_DSN, Secret) and SENTRY_DSN.__str__() not in ("None", ""):
    app.add_middleware(SentryAsgiMiddleware)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8888, log_level="info")
