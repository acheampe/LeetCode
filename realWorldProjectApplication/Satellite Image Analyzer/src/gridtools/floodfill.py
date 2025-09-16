from collections import deque
from collections.abc import Callable

from gridtools.predicates import (
    is_within_bound,
    is_water,
)

# calling a function with args [int, int, list[list[int]]] that returns a list[tuple[int, int]]
NeighborFn = Callable[[int, int, list[list[int]]], list[tuple[int, int]]]

# utilizing BFS approach to overcome python's 1,000 recursion depth limit
def floodfill(k: int, l: int, curr_grid: list[list[int]], neighbor_fn: NeighborFn):
    """
    Floodfill traversal for water regions in a grid.

    DESIGN INTENT
    -------------
    - This function is deliberately kept *generic and minimal*:
      it only finds and returns all connected water cells starting
      from a given coordinate (k, l).
    - "Connected" is defined by the `neighbor_fn` passed in
      (e.g., `neighbors_4` for 4-directional adjacency, 
      or `neighbors_8` for 8-directional adjacency).
    - The function does not:
        * check whether a region touches the grid edge
        * compute sizes, counts, or enclosed status
        * mutate the grid beyond visitation bookkeeping
      Those concerns belong in higher-level feature modules
      (e.g., `count_water_bodies`, `max_water_area`, etc.).

    PARAMETERS
    ----------
    k, l : int
        Starting row and column coordinates.
    curr_grid : list[list[int]]
        The binary grid (0 = land, 1 = water).
    neighbor_fn : Callable
        Function returning neighbors of a cell given (i, j, grid).
        Typically `neighbors_4` or `neighbors_8`.

    RETURNS
    -------
    list[tuple[int, int]]
        A list of coordinates belonging to the connected water
        region. Returned order is traversal-dependent and not guaranteed.

    NOTES
    -----
    - BFS implementation is used here for clarity and to avoid 
      recursion depth limits.
    - Caller is responsible for interpreting the returned list
      (e.g., computing area, marking cells, or checking edge-contact).
    """
    
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
                

### DFS APPROACH ###
# def floodfill_recursive(
#     r: int,
#     c: int,
#     grid: list[list[int]],
#     neighbor_fn: NeighborFn,
#     visited: set[tuple[int, int]] | None = None
# ) -> list[tuple[int, int]]:
#     """Recursive DFS floodfill returning all connected water cells."""

#     if visited is None:
#         visited = set()

#     # base case: out of bounds, not water, or already seen
#     if not is_within_bound(r, c, grid) or not is_water(r, c, grid) or (r, c) in visited:
#         return []

#     # mark current as visited
#     visited.add((r, c))
#     cells = [(r, c)]

#     # recursively explore neighbors
#     for nr, nc in neighbor_fn(r, c, grid):
#         cells.extend(floodfill_recursive(nr, nc, grid, neighbor_fn, visited))

#     return cells