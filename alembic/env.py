from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
import sys
import os

# Это добавляет директорию вашего проекта в системный путь, убедитесь, что путь корректен
sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), '..')))

# Импорт базы и моделей
from database.engine import engine, Base  # Убедитесь, что engine правильно импортирован

# Alembic Config объект
config = context.config

# Можно раскомментировать, чтобы вести логирование Alembic
# fileConfig(config.config_file_name)

# Указываем метаданные
target_metadata = Base.metadata

def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True, dialect_opts={"paramstyle": "named"}
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
