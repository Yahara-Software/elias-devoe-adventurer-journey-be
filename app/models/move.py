from typing import Literal, get_args
from dataclasses import dataclass
from sqlalchemy import ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column, composite

from app.models.base import Base


DIRECTIONS = Literal["F", "B", "R", "L"]
ALLOWED_DIRECTIONS = get_args(DIRECTIONS)

@dataclass
class Position:
    x: int
    y: int


class Move(Base):
    """A single move for an adventurer."""

    __tablename__ = "moves"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    adventurer_id: Mapped[str] = mapped_column(ForeignKey("adventurers.id"), index=True)
    heading: Mapped[DIRECTIONS] = mapped_column(
        Enum(*ALLOWED_DIRECTIONS, name="direction_enum", create_constraint=True)
    )
    
    prev_x: Mapped[int] = mapped_column()
    prev_y: Mapped[int] = mapped_column()
    x: Mapped[int] = mapped_column()
    y: Mapped[int] = mapped_column()
    
    previous_position: Mapped[Position] = composite(Position, "prev_x", "prev_y")
    position: Mapped[Position] = composite(Position, "x", "y")
    
    magnitude: Mapped[int] = mapped_column()
    dist: Mapped[float] = mapped_column()
