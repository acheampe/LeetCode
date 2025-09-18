from gridtools.predicates import (
    is_water,
    is_land
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
    m: int = len(grid)
    
    if not m:
        return max_area
    
    n: int = len(grid[0])
    if not n:
        return max_area
    
    visited: set[tuple[int, int]] = set()
    
    for i in range(m):
        for j in range(n):
            
            if (i, j) not in visited and is_water(i, j, grid):
                cells_to_sum_area = floodfill(i, j, grid, neighbor_fn)
                max_area = max(max_area, len(cells_to_sum_area)) # calc area via length of returned cells
                visited.update(cells_to_sum_area)
            
    return max_area