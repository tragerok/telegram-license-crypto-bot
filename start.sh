#!/bin/bash

# Скрипт запуска Telegram бота

set -e

echo "Starting Telegram License & Crypto Bot..."

# Проверяем наличие .env файла
if [ ! -f .env ]; then
    echo "Error: .env file not found!"
    echo "Please copy .env.example to .env and fill in your configuration."
    exit 1
fi

# Ждем готовности базы данных
echo "Waiting for PostgreSQL..."
while ! pg_isready -h ${DB_HOST:-postgres} -p ${DB_PORT:-5432} -U ${DB_USER:-postgres} -q; do
    echo "PostgreSQL is unavailable - sleeping"
    sleep 2
done

echo "PostgreSQL is ready!"

# Ждем готовности Redis
echo "Waiting for Redis..."
until redis-cli -h ${REDIS_HOST:-redis} -p ${REDIS_PORT:-6379} ping; do
    echo "Redis is unavailable - sleeping"
    sleep 2
done

echo "Redis is ready!"

# Применяем миграции базы данных (если есть)
if [ -f "database/migrations/init.sql" ]; then
    echo "Applying database migrations..."
    export PGPASSWORD=${DB_PASSWORD:-postgres}
    psql -h ${DB_HOST:-postgres} -U ${DB_USER:-postgres} -d ${DB_NAME:-telegram_bot} -f database/migrations/init.sql || echo "Migrations may have already been applied"
    unset PGPASSWORD
fi

# Запускаем бота
echo "Starting bot..."
exec python bot.py
