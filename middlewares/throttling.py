from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware
from aiogram.types import Message
from datetime import datetime

from utils.redis_client import redis


class ThrottlingMiddleware(BaseMiddleware):
    THROTTLE_TIME = 10  # seconds

    def __init__(self):
        self.redis = redis

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        user_id = str(event.from_user.id)

        # Проверяем троттлинг и получаем оставшееся время
        is_throttled, time_left = self.redis.check_throttle(
            user_id=user_id
        )

        if is_throttled:
            await event.answer(
                f"⏳ Вы можете отправлять код только раз в 10 секунд.\n"
                f"Подождите ещё {time_left} сек."
            )
            return

        # Устанавливаем троттлинг на 10 секунд
        self.redis.set_throttle(
            user_id=user_id,
            throttle_time=self.THROTTLE_TIME
        )

        return await handler(event, data)
