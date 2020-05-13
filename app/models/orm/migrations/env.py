# isort:skip_file

import sys

sys.path.extend(["./"])

from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context

from app.settings.globals import ALEMBIC_CONFIG

######################## --- MODELS FOR MIGRATIONS --- ########################
from app.application import db
from app.models.orm.user import User

# To include a model in migrations, add a line here.
# from app.models.orm.person import Person

###############################################################################

config = context.config
fileConfig(config.config_file_name)
target_metadata = db


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    context.configure(
        url=ALEMBIC_CONFIG.url.__to_string__(hide_password=False),
        target_metadata=target_metadata,
        literal_binds=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        {
            "sqlalchemy.url": ALEMBIC_CONFIG.url.__to_string__(
                hide_password=False
            )
        },
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
