from collections import deque
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

# utilizing BFS approach to overcome python's 1,000 recursion depth limit
def floodfill(k: int, l: int, curr_grid: list[list[int]], neighbor_fn: NeighborFn):
    """returns all connected lake cells in grid"""
    
    # defensive assertions
    assert len(curr_grid) > 0, f"No rows found in {curr_grid}"
    assert len(curr_grid[0]) > 0, f"No column found in {curr_grid}"
    
    explore_nei = deque()
    valid_nei: list[tuple[int, int]] = []
    
    mark_visited: set = set()
    
    # check curr coords if land (0) or water (1)
    if is_within_bound(k, l, curr_grid) and is_water(k, l, curr_grid):
        explore_nei.append((k, l))

    while explore_nei:
        
        qr, qc = explore_nei.popleft()
        
        if is_water(qr, qc, curr_grid) and (qr, qc) not in mark_visited:
            valid_nei.append((qr, qc))
            mark_visited.add((qr, qc))
            next_neigbors = neighbor_fn(qr, qc, curr_grid)
            
            for coord in next_neigbors:
                explore_nei.append(coord)
            
    return valid_nei
                

# def landfill(k: int, l: int, curr_grid: list[list[int]]):
#     return fill(k, l, curr_grid)