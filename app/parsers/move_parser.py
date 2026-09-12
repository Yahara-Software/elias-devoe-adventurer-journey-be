import math
from dataclasses import dataclass
from typing import List

from app.errors.errors import MalformedDirectionError
from app.models.move import DIRECTIONS, ALLOWED_DIRECTIONS, Position

@dataclass
class MoveData:
    """A parsed move, ready to be persisted as a `Move` row."""
    heading: str
    magnitude: int
    dist: float
    previous_position: Position
    position: Position


def my_parse_int(num: str) -> int:
    """
    To remind myself how it's done.
    
    No error handling. Assumes num is a string of only digits.
    """
    res = 0
    for c in num:
        res = res * 10 + ord(c) - ord('0')
    return res


def euclidean_distance(pos: Position) -> int:
    """
    Returns the 2D euclidean distance from a position to the origin
    """
    return math.sqrt(pos.x * pos.x + pos.y * pos.y)


def move_adventurer(n_steps: int, heading: DIRECTIONS, pos: Position) -> MoveData:
    """
    Updates adventurer position n_steps in the heading direction
    """
    new_x, new_y = 0, 0
    if heading == "F":
        new_x = pos.x + n_steps
        new_y = pos.y
    elif heading == "B":
        new_x = pos.x - n_steps
        new_y = pos.y
    elif heading == "R":
        new_x = pos.x
        new_y = pos.y + n_steps
    elif heading == "L":
        new_x = pos.x
        new_y = pos.y - n_steps
    
    new_pos = Position(new_x, new_y)
    new_dist = euclidean_distance(new_pos)
    move = MoveData(
        heading=heading,
        previous_position=pos,
        magnitude=n_steps,
        dist=new_dist,
        position=new_pos
    )
    return move


def aggregate_moves(directions, curr_pos) -> List[MoveData]:
    """ 
    Aggregates consecutive adventurer moves.
    
    Returns the list of moves made by the adventurer
    """
    
    res = []
    curr_num = ""
    for i, c in enumerate(directions):
        if c.isdigit():
            curr_num += c
        else:
            if not len(curr_num):
                raise MalformedDirectionError(
                    f"Malformed directions: missing number of steps before {c} at position {i}."
                )
            
            if c not in ALLOWED_DIRECTIONS:
                raise MalformedDirectionError(
                    f"Malformed directions: unknown direction {c} at position {i}."
                )
            
            curr_num = my_parse_int(curr_num)
            curr_move = move_adventurer(curr_num, c, curr_pos)
            res.append(curr_move)
            curr_pos = curr_move.position
            curr_num = ""
    
    if len(curr_num):
        raise MalformedDirectionError(
            f"Malformed directions: missing final direction."
        )
    
    return res
            
        
        