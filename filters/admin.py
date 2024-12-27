from aiogram.filters import BaseFilter
from aiogram.types import Message
from typing import Union

from config.config import project_config


class AdminFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in project_config.ADMIN_IDS
