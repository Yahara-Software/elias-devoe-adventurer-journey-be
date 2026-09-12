"""movement_controller.py
"""

from flask import Blueprint, jsonify, request

from app.db import get_session
from app.errors.errors import MalformedPayloadError
from app.services.move_service import MoveService
from app.services.adventurer_service import AdventurerService
from app.use_cases.get_adventurer_moves_use_case import GetAdventurerMovesUseCase
from app.use_cases.move_adventurer_use_case import MoveAdventurerUseCase


adventurer_bp = Blueprint("adventurer", __name__)

_move_service = MoveService()
_adventurer_service = AdventurerService()
_get_adventurer_moves_use_case = GetAdventurerMovesUseCase(_adventurer_service, _move_service)
_move_adventurer_use_case = MoveAdventurerUseCase(_move_service)


@adventurer_bp.route("/<adventurer_id>/make_moves", methods=["POST"])
def save_adventurer_move(adventurer_id: str):
    body = request.get_json(silent=True) or {}
    moves = body.get("moves")
    if not moves:
        raise MalformedPayloadError(
            "Request body must include 'moves'"
        )

    session = get_session()
    all_moves = _move_adventurer_use_case.execute(
        session, adventurer_id, moves
    )
    return jsonify([move.serialize() for move in all_moves]), 201


@adventurer_bp.route("/<adventurer_id>/get_moves", methods=["GET"])
def get_adventurer_moves(adventurer_id: str):
    session = get_session()
    moves = _get_adventurer_moves_use_case.execute(
        session, adventurer_id
    )
    return jsonify([move.serialize() for move in moves])

