from sqlalchemy import select

from database.models import Prize
from repositories.base import Repository


class PrizeRepository(Repository):
    async def check_code_status(self, code: str):
        query = select(Prize).where(
            Prize.code == code
        )
        result = await self.db.execute(query)
        return result.scalar_one_or_none()

    async def edit_code_status(self, code: str):
        query = select(Prize).where(
            Prize.code == code
        ).with_for_update()
        result = await self.db.execute(query)

        code = result.scalar_one_or_none()

        if code is not None:
            code.is_used = True

        await self.db.commit()

    async def set_winner(self, code: str, winner: str | None):
        query = select(Prize).where(
            Prize.code == code
        ).with_for_update()
        result = await self.db.execute(query)

        code = result.scalar_one_or_none()

        if code is not None:
            code.winner = winner

        await self.db.commit()