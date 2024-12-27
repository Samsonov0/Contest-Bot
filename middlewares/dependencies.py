from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery

class DependencyMiddleware(BaseMiddleware):
    def __init__(self, session, **kwargs):
        super().__init__()
        self.session = session
        self.additional_deps = kwargs

    async def __call__(
        self,
        handler: Callable[[Message | CallbackQuery, Dict[str, Any]], Awaitable[Any]],
        event: Message | CallbackQuery,
        data: Dict[str, Any]
    ) -> Any:
        # Добавляем сессию в данные
        async with self.session() as session:
            data['session'] = session
            # Добавляем дополнительные зависимости
            data.update(self.additional_deps)
            return await handler(event, data)