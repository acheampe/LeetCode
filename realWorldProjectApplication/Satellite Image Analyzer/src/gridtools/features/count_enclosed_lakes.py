from gridtools.predicates import (
    is_water, 
    is_interior_coord,
    is_edge_coord
)

from gridtools.floodfill import (
    NeighborFn,
    floodfill
)

def count_enclosed_lakes(grid: list[list[int]], neighbor_fn: NeighborFn) -> int:
    """_summary_

    Args:
        grid (list[list[int]]): Count distinct lake bodies (connected groups of 1s) that 
        does not touch edges of grid, using the given neighbor function.
        
    Returns:
        int: returns the amount of separate lakes provided in image
    """
    
    count_enclosed: int= 0
    
    return count_enclosed