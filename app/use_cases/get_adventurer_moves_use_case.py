

"""get_adventurer_moves_use_case.py

Retrieve the moves for a particular adventurer.
"""

from sqlalchemy.orm import Session
from app.errors.errors import AdventurerNotFoundError

from app.services.adventurer_service import AdventurerService
from app.services.move_service import MoveService

from app.models.move import Move


class GetAdventurerMovesUseCase:
    def __init__(self, adventurer_service: AdventurerService, move_service: MoveService):
        self.adventurer_service = adventurer_service
        self.move_service = move_service

    def execute(
        self, 
        session: Session, 
        adventurer_id: str,
    ) -> list[Move]:
        if not self.adventurer_service.adventurer_exists(session, adventurer_id):
            raise AdventurerNotFoundError(f"No adventurer found with id '{adventurer_id}'")
    
        return self.move_service.get_adventurer_moves(
            session, adventurer_id
        )
