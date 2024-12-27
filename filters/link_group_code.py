from aiogram.filters import Filter
from aiogram.types import Message


class LinkGroupCommand(Filter):
    async def __call__(self, message: Message) -> bool | dict:
        if not message.text.startswith('/link_group'):
            return False

        try:
            # Извлекаем id из команды /link_group?code554234
            code = message.text.split('?code')[1]
            return {'code': int(code)}
        except IndexError:
            return False
