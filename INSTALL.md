# Telegram License & Crypto Bot - Installation Guide

## Требования к системе

### Минимальные требования
- **ОС**: Linux (Ubuntu 20.04+, Debian 11+, CentOS 8+) или macOS
- **CPU**: 2 ядра
- **RAM**: 2 GB
- **Диск**: 10 GB свободного места
- **Docker**: 20.10+
- **Docker Compose**: 2.0+

### Программное обеспечение
- Python 3.11+ (для локального запуска)
- PostgreSQL 15+ (если без Docker)
- Redis 7+ (если без Docker)
- Git

## Установка с помощью Docker (Рекомендуется)

### Шаг 1: Клонирование репозитория

```bash
git clone https://github.com/tragerok/telegram-license-crypto-bot.git
cd telegram-license-crypto-bot
```

### Шаг 2: Настройка переменных окружения

```bash
cp .env.example .env
```

Откройте файл `.env` и заполните необходимые переменные:

```bash
# Telegram Bot Configuration
BOT_TOKEN=your_bot_token_here
ADMIN_IDS=123456789,987654321

# Database Configuration
DB_HOST=postgres
DB_PORT=5432
DB_NAME=telegram_bot
DB_USER=postgres
DB_PASSWORD=your_secure_password

# Redis Configuration
REDIS_HOST=redis
REDIS_PORT=6379

# Cryptocurrency API Keys
COINGATE_API_KEY=your_coingate_key
BINANCE_API_KEY=your_binance_key
BINANCE_SECRET_KEY=your_binance_secret

# Web3 Configuration (optional)
ETH_NODE_URL=https://mainnet.infura.io/v3/your_project_id
BTC_NODE_URL=your_bitcoin_node_url

# FastAPI Configuration
API_HOST=0.0.0.0
API_PORT=8000
SECRET_KEY=your_secret_key_for_jwt
```

### Шаг 3: Запуск с помощью Docker Compose

```bash
# Сборка и запуск всех сервисов
docker-compose up -d --build

# Проверка статуса контейнеров
docker-compose ps

# Просмотр логов
docker-compose logs -f bot
```

### Шаг 4: Проверка работоспособности

```bash
# Проверить, что бот запущен
docker-compose logs bot

# Проверить подключение к базе данных
docker-compose exec postgres psql -U postgres -d telegram_bot -c "\dt"

# Проверить Redis
docker-compose exec redis redis-cli ping
```

### Остановка и удаление

```bash
# Остановка всех сервисов
docker-compose stop

# Остановка и удаление контейнеров
docker-compose down

# Удаление контейнеров и volumes (ВНИМАНИЕ: удалит все данные)
docker-compose down -v
```

## Установка без Docker (Локальный запуск)

### Шаг 1: Установка Python зависимостей

```bash
# Создание виртуального окружения
python3.11 -m venv venv
source venv/bin/activate  # для Linux/macOS
# или
venv\Scripts\activate  # для Windows

# Установка зависимостей
pip install --upgrade pip
pip install -r requirements.txt
```

### Шаг 2: Установка PostgreSQL

#### Ubuntu/Debian
```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
sudo systemctl start postgresql
sudo systemctl enable postgresql
```

#### macOS (с Homebrew)
```bash
brew install postgresql@15
brew services start postgresql@15
```

### Шаг 3: Создание базы данных

```bash
# Войти в PostgreSQL
sudo -u postgres psql

# Создать базу данных и пользователя
CREATE DATABASE telegram_bot;
CREATE USER botuser WITH PASSWORD 'your_password';
ALTER ROLE botuser SET client_encoding TO 'utf8';
ALTER ROLE botuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE botuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE telegram_bot TO botuser;
\q

# Применить миграции
export PGPASSWORD='your_password'
psql -h localhost -U botuser -d telegram_bot -f database/migrations/init.sql
```

### Шаг 4: Установка Redis

#### Ubuntu/Debian
```bash
sudo apt install redis-server
sudo systemctl start redis
sudo systemctl enable redis
```

#### macOS (с Homebrew)
```bash
brew install redis
brew services start redis
```

### Шаг 5: Настройка .env файла

```bash
cp .env.example .env
# Отредактируйте .env, указав:
# DB_HOST=localhost
# REDIS_HOST=localhost
# и другие необходимые параметры
```

### Шаг 6: Запуск бота

```bash
# Активировать виртуальное окружение (если еще не активировано)
source venv/bin/activate

# Запустить бота
python bot.py

# Или использовать start.sh (после chmod +x start.sh)
./start.sh
```

## Получение Telegram Bot Token

1. Откройте Telegram и найдите бота [@BotFather](https://t.me/botfather)
2. Отправьте команду `/newbot`
3. Следуйте инструкциям для создания бота
4. Скопируйте полученный токен и добавьте его в `.env` файл

```
BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrsTUVwxyz
```

## Настройка API ключей для криптовалют

### CoinGate
1. Зарегистрируйтесь на [CoinGate](https://coingate.com/)
2. Перейдите в раздел API
3. Создайте новый API ключ
4. Добавьте ключ в `.env`:
```
COINGATE_API_KEY=your_key_here
```

### Binance Pay (опционально)
1. Зарегистрируйтесь на [Binance](https://www.binance.com/)
2. Перейдите в API Management
3. Создайте API ключ с правами на Pay
4. Добавьте ключи в `.env`:
```
BINANCE_API_KEY=your_api_key
BINANCE_SECRET_KEY=your_secret_key
```

## Проверка установки

### Тестовые команды

```bash
# Проверить подключение к базе данных
python -c "from database import check_connection; check_connection()"

# Проверить подключение к Redis
redis-cli ping

# Запустить бота в режиме отладки
export LOG_LEVEL=DEBUG
python bot.py
```

### Проверка через Telegram

1. Найдите вашего бота в Telegram
2. Отправьте команду `/start`
3. Проверьте, что бот отвечает

## Troubleshooting (Решение проблем)

### Бот не запускается

**Проблема**: `ModuleNotFoundError: No module named 'aiogram'`

**Решение**:
```bash
pip install -r requirements.txt
```

**Проблема**: `Connection refused` при подключении к PostgreSQL

**Решение**:
```bash
# Проверьте, что PostgreSQL запущен
sudo systemctl status postgresql

# Проверьте настройки в .env
# Убедитесь, что DB_HOST, DB_PORT, DB_USER, DB_PASSWORD корректны
```

**Проблема**: `Error: Invalid token`

**Решение**: Проверьте правильность BOT_TOKEN в `.env` файле

### База данных не создается

**Решение**:
```bash
# Пересоздать базу данных
docker-compose down -v
docker-compose up -d

# Или вручную применить миграции
docker-compose exec postgres psql -U postgres -d telegram_bot -f /docker-entrypoint-initdb.d/init.sql
```

### Бот работает медленно

**Проверьте**:
1. Доступность Redis
2. Нагрузку на сервер
3. Логи бота на наличие ошибок

## Обновление бота

### С Docker

```bash
# Получить последние изменения
git pull origin main

# Пересобрать и перезапустить
docker-compose up -d --build
```

### Без Docker

```bash
# Получить последние изменения
git pull origin main

# Обновить зависимости
source venv/bin/activate
pip install -r requirements.txt --upgrade

# Применить новые миграции (если есть)
psql -h localhost -U botuser -d telegram_bot -f database/migrations/migration_002.sql

# Перезапустить бота
pkill -f bot.py
python bot.py
```

## Резервное копирование

### Backup базы данных

```bash
# С Docker
docker-compose exec postgres pg_dump -U postgres telegram_bot > backup_$(date +%Y%m%d).sql

# Без Docker
pg_dump -h localhost -U botuser telegram_bot > backup_$(date +%Y%m%d).sql
```

### Восстановление из backup

```bash
# С Docker
docker-compose exec -T postgres psql -U postgres telegram_bot < backup_20251001.sql

# Без Docker
psql -h localhost -U botuser telegram_bot < backup_20251001.sql
```

## Мониторинг

### Логи

```bash
# Docker логи
docker-compose logs -f --tail=100 bot

# Локальные логи
tail -f logs/bot.log
```

### Метрики

Бот сохраняет логи в директории `logs/`:
- `bot.log` - основные логи
- `errors.log` - логи ошибок
- `transactions.log` - логи транзакций

## Безопасность

### Рекомендации

1. **Никогда не коммитьте `.env` файл в Git**
2. Используйте сильные пароли для базы данных
3. Регулярно обновляйте зависимости
4. Используйте HTTPS для API
5. Настройте firewall для ограничения доступа к портам
6. Регулярно делайте backup базы данных

### Firewall настройки (UFW)

```bash
# Разрешить только SSH, HTTP, HTTPS
sudo ufw allow ssh
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable

# Закрыть прямой доступ к PostgreSQL и Redis из интернета
# (они должны быть доступны только внутри Docker сети)
```

## Поддержка

Если у вас возникли проблемы:

1. Проверьте [Issues](https://github.com/tragerok/telegram-license-crypto-bot/issues)
2. Создайте новый Issue с описанием проблемы
3. Приложите логи и конфигурацию (без приватных данных)

## Полезные ссылки

- [Документация Telegram Bot API](https://core.telegram.org/bots/api)
- [Документация Aiogram](https://docs.aiogram.dev/)
- [Документация PostgreSQL](https://www.postgresql.org/docs/)
- [Документация Redis](https://redis.io/documentation)
- [Документация Docker Compose](https://docs.docker.com/compose/)

---

**Удачи в запуске вашего бота! 🚀**
