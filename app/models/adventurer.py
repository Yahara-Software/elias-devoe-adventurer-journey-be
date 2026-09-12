from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class Adventurer(Base):
    """An adventurer who may move around the grid."""

    __tablename__ = "adventurers"

    id: Mapped[str] = mapped_column(String, primary_key=True)
