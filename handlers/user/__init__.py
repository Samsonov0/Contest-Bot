from aiogram import Router
# from .start import router as start_router
# from .profile import router as profile_router
# from .settings import router as settings_router
# from .help import router as help_router
from .base import router as base_router

user_router = Router()  # Изменили имя на user_router
user_router.include_router(base_router)
# router.include_router(profile_router)
# router.include_router(settings_router)
# router.include_router(help_router)
