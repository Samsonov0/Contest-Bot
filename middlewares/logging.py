import logging
from typing import Callable, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message


class LoggingMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: dict[str, Any]
    ) -> Any:
        user_id = event.from_user.id
        username = event.from_user.username
        logging.info(f"User {username} ({user_id}) sent: {event.text}")
        return await handler(event, data)
