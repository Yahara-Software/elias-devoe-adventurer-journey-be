"""adventurer_service.py

Minimal service for checking if adventurer exists.
"""

from sqlalchemy.orm import Session
from app.models.adventurer import Adventurer


class AdventurerService:
    def adventurer_exists(self, session: Session, adventurer_id: str) -> bool:
        return session.get(Adventurer, adventurer_id) is not None
