import enum

from sqlalchemy import Column, Integer, String, DateTime, func, UUID, ForeignKey, BigInteger, Enum, Boolean
from sqlalchemy.orm import relationship

from database.session import Base


class Prize(Base):
    __tablename__ = "prizes"

    id = Column(Integer, autoincrement=True, primary_key=True)
    code = Column(String, nullable=False, unique=True)
    created_by_channel = Column(String, nullable=False)
    ask_to_prize = Column(String, nullable=False)
    is_used = Column(Boolean, default=False)
    prize = Column(String, nullable=False)
    winner = Column(String, nullable=True)
