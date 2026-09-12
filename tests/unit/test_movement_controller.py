import pytest
import math

from app.controllers.movement_controller import aggregate_moves
from app.errors.errors import MalformedDirectionError



def test_non_digit_start_raises():
    directions = "U7L"
    with pytest.raises(MalformedDirectionError):
        aggregate_moves(directions)


def test_non_allowed_direction_raises():
    directions = "70-"
    with pytest.raises(MalformedDirectionError):
        aggregate_moves(directions)


def test_subsequent_directions_raises():
    directions = "7UD"
    with pytest.raises(MalformedDirectionError):
        aggregate_moves(directions)


def test_missing_final_direction_raises():
    directions = "7U4D2"
    with pytest.raises(MalformedDirectionError):
        aggregate_moves(directions)


# TODO handle int overflow?


def test_correct_string():
    # Sanity check an easy one
    directions = "1F1B1R1L"
    heading, position, dist = aggregate_moves(directions)
    assert position == (0, 0)
    assert dist == 0
    assert heading == "L"
    
    # Then do the problem
    directions = "15F6B6B5L16R8B16F20L6F13F11R"
    heading, position, dist = aggregate_moves(directions)
    assert position == (30, 2)
    assert math.isclose(round(dist, 4), 30.0666)
