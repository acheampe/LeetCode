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
    
    m, n = len(grid), len(grid[0])
    body_count: int = 0
    
    if not m or not n:
        return 0 
    
    explored_path: set = set()
    
    for i in range(m):
        for j in range(n):
            
            if (i, j) not in explored_path:
                accrued_body: list[tuple[int, int]] = floodfill(i, j, grid, neighbor_fn)
                if accrued_body:
                    body_count += 1
                    for coord in accrued_body:
                        explored_path.add(coord)
                    
    
    return body_count