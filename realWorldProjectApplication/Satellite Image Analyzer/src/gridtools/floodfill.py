from collections.abc import Callable 

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

# calling a function with args [int, int, list[list[int]]] that returns a list[tuple[int, int]]
NeighborFn = Callable[[int, int, list[list[int]]], list[tuple[int, int]]]

def floodfill(k: int, l: int, curr_grid: list[list[int]], neighbor_fn: NeighborFn):

    valid_nei: list[tuple[int, int]] = []
    
    # check curr coords if land (0) or water (1)
    if is_within_bound(k, l, curr_grid) and is_water(k, l, curr_grid):
        valid_nei.append((k, l))
        curr_nei: list[tuple[int, int]] = neighbor_fn(k, l, curr_grid)
    
        for nei in curr_nei:
            r, c = nei
            if is_water(r, c, curr_grid):
                valid_nei.append((r, c))
    
    return valid_nei
                

# def landfill(k: int, l: int, curr_grid: list[list[int]]):
#     return fill(k, l, curr_grid)