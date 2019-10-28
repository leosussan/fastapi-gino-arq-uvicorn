from importlib import import_module

from app.application import db
from app.settings.arq import settings
from app.settings.globals import DATABASE_CONFIG, ARQ_BACKGROUND_FUNCTIONS


FUNCTIONS: list = [
    getattr(import_module(function_path), function_name)
    for function_path, function_name in [
        background_function.rsplit(".", 1)
        for background_function in list(ARQ_BACKGROUND_FUNCTIONS)
    ]
] if ARQ_BACKGROUND_FUNCTIONS is not None else list()


async def startup(ctx):
    """
    Binds a connection set to the db object.
    """
    await db.set_bind(DATABASE_CONFIG.url)


async def shutdown(ctx):
    """
    Pops the bind on the db object.
    """
    await db.pop_bind().close()


class WorkerSettings:
    """
    Settings for the ARQ worker.
    """

    on_startup = startup
    on_shutdown = shutdown
    redis_settings = settings
    functions: list = FUNCTIONS
