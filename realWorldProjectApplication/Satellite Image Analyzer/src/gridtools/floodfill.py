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

def fill(i: int, j: int, grid: list[list[int]]) -> list[tuple[int, int]]:
    """returns all neighbors per directions"""
    return neighbors_4(i, j, grid)

def floodfill(k: int, l: int, curr_grid: list[list[int]]):

    valid_nei: list[tuple[int, int]] = []
    
    # check curr coords if land (0) or water (1)
    if is_within_bound(k, l, curr_grid) and curr_grid[k][l] == 1:
        valid_nei.append((k, l))
        curr_nei = fill(k, l, curr_grid)
    
        for nei in curr_nei:
            r, c = nei
            if curr_grid[r][c] == 1:
                valid_nei.append((r, c))
    
    return valid_nei
                

# def landfill(k: int, l: int, curr_grid: list[list[int]]):
#     return fill(k, l, curr_grid)