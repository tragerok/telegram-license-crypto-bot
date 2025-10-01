import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config import Config
from handlers import register_handlers
from database import init_db
from middlewares import setup_middlewares

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

async def main():
    """Main bot startup function"""
    try:
        # Initialize config
        config = Config()
        
        # Initialize database
        await init_db()
        logger.info("Database initialized")
        
        # Initialize bot and dispatcher
        bot = Bot(token=config.BOT_TOKEN)
        storage = MemoryStorage()
        dp = Dispatcher(storage=storage)
        
        # Setup middlewares
        setup_middlewares(dp)
        
        # Register handlers
        register_handlers(dp)
        
        logger.info("Bot started successfully")
        
        # Start polling
        await dp.start_polling(bot)
        
    except Exception as e:
        logger.error(f"Error starting bot: {e}")
        raise
    finally:
        await bot.session.close()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Bot stopped by user")
