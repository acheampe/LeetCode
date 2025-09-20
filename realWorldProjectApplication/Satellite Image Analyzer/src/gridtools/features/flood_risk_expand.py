from gridtools.predicates import (
    is_water,
    is_land
)

from gridtools.floodfill import (
    NeighborFn,
)

def flood_risk_expand(grid: list[list[int]], neighbor_fn: NeighborFn) -> list[tuple[int, int]]:
    """Return list of unique flood risk land cells adjacent to any water cell."""

    if not grid or not grid[0]:
        return []

    m, n = len(grid), len(grid[0])
    risk_zones: set[tuple[int, int]] = set()
    visited: set[tuple[int, int]] = set()  # tracks visited water cells

    for i in range(m):
        for j in range(n):

            if is_water(i, j, grid):
                for r, c in neighbor_fn(i, j, grid):
                    if is_land(r, c, grid):
                        risk_zones.add((r, c))

    return list(risk_zones)