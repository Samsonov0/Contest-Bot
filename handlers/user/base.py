from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config.config import project_config
from repositories.prize import PrizeRepository

from utils.i18n import i18n

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message, session, state: FSMContext):
    channels = "https://t.me/NoobaPieAdventure"

    await message.answer(
        i18n.get(
            key="welcome",
            channels=channels
        ),
        parse_mode="HTML"
    )


@router.message(F.text)
async def check_code(message: Message, session, state: FSMContext):
    code = message.text.strip()

    prize_repository = PrizeRepository(
        db=session
    )

    code_data = await prize_repository.check_code_status(
        code=code
    )

    if code_data is None:
        channels = "https://t.me/NoobaPieAdventure"

        await message.answer(
            i18n.get(
                key="incorrect_code",
                channels=channels
            ),
            parse_mode="HTML"
        )

    is_used = code_data.is_used

    if is_used:
        await message.answer(
            i18n.get(
                key="code_is_used",
                channel=code_data.created_by_channel
            ),
            parse_mode="HTML"
        )

    elif not is_used:
        await message.answer(
            i18n.get(
                key="code_is_not_used",
                prize=code_data.prize,
                channel=code_data.created_by_channel,
                ask_for_prize=code_data.ask_to_prize
            ),
            parse_mode="HTML"
        )

        await prize_repository.edit_code_status(
            code=code
        )
        await prize_repository.set_winner(
            code=code,
            winner=message.from_user.username
        )

    return

