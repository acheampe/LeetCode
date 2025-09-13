from gridtools.connectivity import (
    neighbors_4, 
    neighbors_8,
)
from gridtools.predicates import (
    is_within_bound,
    is_water,
    is_land,
    is_edge_coord,
    is_interior_coord,
)

def fill(i: int, j: int, grid: list[list[int]]):
    return []

def floodfill(k: int, l: int, curr_grid: list[list[int]]):
    return fill(k, l, curr_grid)

def landfill(k: int, l: int, curr_grid: list[list[int]]):
    return fill(k, l, curr_grid)