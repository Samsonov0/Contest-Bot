from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config.config import project_config
from utils.i18n import i18n


async def bot_send_message(chat_id: int, key: str, lang, **kwargs):
    default = DefaultBotProperties(
        parse_mode=ParseMode.HTML,
        protect_content=False,
    )

    bot = Bot(
        token=project_config.BOT_TOKEN,
        default=default
    )

    await bot.send_message(
        chat_id=chat_id,
        text=i18n.get(
            key=key,
            lang=lang,
            **kwargs
        ),
        parse_mode="HTML"
    )