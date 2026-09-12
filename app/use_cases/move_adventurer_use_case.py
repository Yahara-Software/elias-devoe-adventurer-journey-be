"""move_adventurer_use_case.py

Orchestrates a movement request: currently just a pass-through
to the service.
"""

from typing import List
from sqlalchemy.orm import Session

from app.parsers.move_parser import aggregate_moves
from app.services.move_service import MoveService
from app.models.move import Move, Position

class MoveAdventurerUseCase:
    def __init__(self, move_service: MoveService):
        self.move_service = move_service
    
    def execute(
        self, session: Session, adventurer_id: str, directions: str
    ) -> List[Move]:
        old_moves = self.move_service.get_adventurer_moves(session, adventurer_id)
        if old_moves:
            prev_pos = old_moves[-1].position
        else:
            prev_pos = Position(0, 0)
        
        moves = aggregate_moves(directions, prev_pos)
        self.move_service.save_moves(session, adventurer_id, moves)
        session.commit()
        new_moves = self.move_service.get_adventurer_moves(session, adventurer_id)
        return new_moves
