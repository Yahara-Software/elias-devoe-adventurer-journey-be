import pytest
import math

from app.models.move import Position
from app.parsers.move_parser import aggregate_moves
from app.errors.errors import MalformedDirectionError



def test_non_digit_start_raises():
    directions = "U7L"
    with pytest.raises(MalformedDirectionError):
        aggregate_moves(directions, Position(0, 0))


def test_non_allowed_direction_raises():
    directions = "70-"
    with pytest.raises(MalformedDirectionError):
        aggregate_moves(directions, Position(0, 0))


def test_subsequent_directions_raises():
    directions = "7UD"
    with pytest.raises(MalformedDirectionError):
        aggregate_moves(directions, Position(0, 0))


def test_missing_final_direction_raises():
    directions = "7U4D2"
    with pytest.raises(MalformedDirectionError):
        aggregate_moves(directions, Position(0, 0))


# TODO handle int overflow?


def test_correct_string():
    # Sanity check an easy one
    directions = "1F1B1R1L"
    moves = aggregate_moves(directions, Position(0, 0))
    last_move = moves[-1]
    heading, position, dist = last_move.heading, last_move.position, last_move.dist
    assert position.x == 0 and position.y == 0
    assert dist == 0
    assert heading == "L"
    
    # Then do the problem
    directions = "15F6B6B5L16R8B16F20L6F13F11R"
    moves = aggregate_moves(directions, Position(0, 0))
    last_move = moves[-1]
    heading, position, dist = last_move.heading, last_move.position, last_move.dist
    assert position.x == 30 and position.y == 2
    assert math.isclose(round(dist, 4), 30.0666)
