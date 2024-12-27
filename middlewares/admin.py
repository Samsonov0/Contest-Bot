from typing import Callable, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message


class AdminMiddleware(BaseMiddleware):
    def __init__(self, admin_ids: list[int]):
        self.admin_ids = admin_ids

    async def __call__(
            self,
            handler: Callable[[Message, dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: dict[str, Any]
    ) -> Any:
        if event.from_user.id not in self.admin_ids:
            await event.answer("Access denied")
            return
        return await handler(event, data)
