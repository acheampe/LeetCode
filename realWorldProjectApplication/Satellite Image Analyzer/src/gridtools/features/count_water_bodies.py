from gridtools.floodfill import NeighborFn, floodfill
from collections.abc import Callable


def count_water_bodies(grid: list[list[int]], neighbor_fn: NeighborFn) -> int:
    """_summary_

    Args:
        i (int): row number of grid coordinate
        j (int): col number of grid coordinate
        grid (list[list[int]]): grid image to analyze count_water bodies

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
            if (i, j) not in visited:
                region = floodfill(i, j, grid, neighbor_fn)
                if region:
                    body_count += 1
                    visited.update(region)
    
    return body_count