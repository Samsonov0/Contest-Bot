import asyncio
import logging
from aiogram import Bot, Dispatcher, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message
from aiogram.filters import Command

from config.config import project_config
from database.session import get_db
from middlewares.db_session import DbSessionMiddleware
from middlewares.dependencies import DependencyMiddleware
from middlewares.logging import LoggingMiddleware
from middlewares.throttling import ThrottlingMiddleware
from handlers import register_all_handlers

# Создаем роутер
main_router = Router()


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(name)s - %(message)s'
    )

    config = project_config

    storage = RedisStorage.from_url(f'{project_config.REDIS_URL}/0') if config.USE_REDIS else MemoryStorage()

    default = DefaultBotProperties(
        parse_mode=ParseMode.HTML,  # или ParseMode.MARKDOWN_V2
        protect_content=False,  # опционально
    )

    # Инициализируем бота с новым синтаксисом
    bot = Bot(
        token=project_config.BOT_TOKEN,
        default=default
    )
    dp = Dispatcher(storage=storage)

    dp.include_router(main_router)

    dp.callback_query.middleware.register(DbSessionMiddleware())
    dp.message.middleware.register(DbSessionMiddleware())

    dp.message.middleware.register(LoggingMiddleware())

    dp.message.middleware.register(ThrottlingMiddleware())

    # Регистрация всех хэндлеров
    register_all_handlers(dp)

    # Инициализация базы данных
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())
