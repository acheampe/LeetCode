from gridtools.predicates import (
    is_water,
)

from gridtools.floodfill import (
    NeighborFn,
    floodfill
)

def max_water_area(grid: list[list[int]], neighbor_fn: NeighborFn) -> int:
    """
    Return the maximum area (size in cells) of any connected water body (1s)
    in the given grid, using the chosen neighbor function.
    """
    if not grid or not grid[0]:
        return 0

    max_area = 0
    visited: set[tuple[int, int]] = set()
    m, n = len(grid), len(grid[0])

    for i in range(m):
        for j in range(n):
            if (i, j) not in visited and is_water(i, j, grid):
                region = floodfill(i, j, grid, neighbor_fn)
                area = len(region)
                max_area = max(max_area, area)
                visited.update(region)

    return max_area