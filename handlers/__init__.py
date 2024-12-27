from aiogram import Router, Dispatcher
from typing import Dict

from .user import user_router

def register_all_handlers(dp: Dispatcher) -> None:
    """
    Регистрирует все хендлеры в диспетчере
    Порядок регистрации важен! Сначала административные, потом пользовательские
    """
    # from handlers.admin import router as admin_router
    # from handlers.user import router as user_router
    # from handlers.errors import router as errors_router

    # Регистрируем все роутеры в правильном порядке
    dp.include_router(user_router)
    # dp.include_router(user_router)
    # dp.include_router(errors_router)
