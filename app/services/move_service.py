"""move_service.py

Business logic for persisting and querying moves.
"""


from sqlalchemy.orm import Session

from app.parsers.move_parser import MoveData

from app.models.move import Move
from app.models.adventurer import Adventurer


class MoveService:
    def save_moves(
        self, session: Session, adventurer_id: str, moves: list[MoveData]
    ) -> int:
        """
        Adds moves for an adventurer.
        
        Caller is responsible for committing changes.
        """
        adventurer = session.get(Adventurer, adventurer_id)
        if adventurer is None:
            adventurer = Adventurer(id=adventurer_id)
            session.add(adventurer)
        
        for move_data in moves:
            move = Move(
                adventurer_id=adventurer_id,
                heading=move_data.heading,
                previous_position=move_data.previous_position,
                magnitude=move_data.magnitude,
                dist=move_data.dist,
                position=move_data.position
            )
            session.add(move)
        
        session.flush()
        return

    def get_adventurer_moves(
        self, 
        session: Session, 
        adventurer_id: str
    ) -> list[Move]:
        query = session.query(Move).filter(Move.adventurer_id == adventurer_id)
        return (
            query.order_by(Move.id)
            .all()
        )

