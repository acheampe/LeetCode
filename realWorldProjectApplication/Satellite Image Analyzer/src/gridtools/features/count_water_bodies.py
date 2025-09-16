from gridtools.floodfill import NeighborFn, floodfill
from gridtools.predicates import is_water


def count_water_bodies(grid: list[list[int]], neighbor_fn: NeighborFn) -> int:
    """_summary_

    Args:
        grid (list[list[int]]): Count distinct water bodies (connected groups of 1s) in the grid, 
        using the given neighbor function.
        
    Returns:
        int: returns the amount of separate bodies of water provides in image
    """
    
    m = len(grid)
    if not m:
        return 0
    n = len(grid[0])
    if not n:
        return 0
    
    body_count = 0
    visited: set[tuple[int, int]] = set()
    
    for i in range(m):
        for j in range(n):
            if (i, j) not in visited and is_water(i, j, grid):
                region = floodfill(i, j, grid, neighbor_fn)
                if region:
                    body_count += 1
                    visited.update(region)
    
    return body_count