import math
from typing import Literal, get_args
from app.errors.errors import MalformedDirectionError

DIRECTIONS = Literal["F", "B", "R", "L"]
ALLOWED_DIRECTIONS = get_args(DIRECTIONS)

def my_parse_int(num: str):
    """
    To remind myself how it's done.
    
    No error handling. Assumes num is a string of only digits.
    """
    res = 0
    for c in num:
        res = res * 10 + ord(c) - ord('0')
    return res


def euclidean_distance(pos: tuple[int, int]):
    """
    Returns the 2D euclidean distance from a position tuple to the origin
    """
    return math.sqrt(pos[0] * pos[0] + pos[1] * pos[1])


def move_adventurer(n_steps: int, heading: DIRECTIONS, pos: tuple[int, int]):
    """
    Updates adventurer position n_steps in the heading direction
    """
    new_x, new_y = 0, 0
    if heading == "F":
        new_x = pos[0] + n_steps
        new_y = pos[1]
    elif heading == "B":
        new_x = pos[0] - n_steps
        new_y = pos[1]
    elif heading == "R":
        new_x = pos[0]
        new_y = pos[1] + n_steps
    elif heading == "L":
        new_x = pos[0]
        new_y = pos[1] - n_steps
    
    new_pos = (new_x, new_y)
    new_dist = euclidean_distance(new_pos)
    return heading, new_pos, new_dist


def aggregate_moves(directions) -> tuple[int, int, int]:
    """ 
    Aggregates consecutive adventurer moves.
    
    Returns the final position, heading, and euclidean distance from origin.
    """
    
    curr_heading = "N"
    curr_position = (0, 0)
    curr_dist = 0
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
            curr_heading, curr_position, curr_dist = move_adventurer(curr_num, c, curr_position)
            curr_num = ""
    
    if len(curr_num):
        raise MalformedDirectionError(
            f"Malformed directions: missing final direction."
        )
    
    return curr_heading, curr_position, curr_dist
            
        
        