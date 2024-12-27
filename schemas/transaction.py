from pydantic import BaseModel, UUID4


class TransactionSchema(BaseModel):
    user_tg_id: int
    stars_amount: int
    crypto_amount: float
    wallet_receiver: str
    cryptocurrency: str
    receiver: str
    memo: int
