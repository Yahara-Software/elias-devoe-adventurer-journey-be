import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.parsers.move_parser import MoveData
from app.models.base import Base
from app.models.move import Position
from app.services.move_service import MoveService


@pytest.fixture
def session():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


def test_save_move_creates_adventurer_and_moves(session):
    service = MoveService()
    moves = [
        MoveData(
            heading="R",
            previous_position=Position(0, 0),
            magnitude=1,
            dist=1,
            position=Position(1, 0)
        )
    ]
    
    service.save_moves(session, "adventurer-1", moves)
    stored = service.get_adventurer_moves(session, "adventurer-1")
    assert len(stored) == 1
