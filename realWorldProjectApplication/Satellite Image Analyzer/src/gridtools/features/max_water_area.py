from gridtools.predicates import (
    is_water, 
)

from gridtools.floodfill import (
    NeighborFn,
    floodfill
)

def max_water_area(grid: list[list[int]], neighbor_fn: NeighborFn) -> int:
    """_summary_

    Args:
        grid (list[list[int]]): Count area of distinct lake bodies 
        (connected groups of 1s - area is sum of distinct region cells) that, 
        using the given neighbor function.
        
    Returns:
        int: returns the max area of body of water in grid
    """
    
    max_area: int = 0
    
    return max_area