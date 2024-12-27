from aiogram.fsm.state import StatesGroup, State


class TransactionState(StatesGroup):
    transaction_id = State()
