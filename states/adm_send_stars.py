from aiogram.fsm.state import StatesGroup, State


class AdmSendStarsState(StatesGroup):
    data = State()
