from gridtools.predicates import (
    is_water,
    is_land
)

from gridtools.floodfill import (
    NeighborFn,
    floodfill
)

def flood_risk_expand(grid: list[list[int]], neighbor_fn: NeighborFn) -> list[tuple[int, int]]:
    """returns a list of flood risk zones in grid"""
    
    global_flood_risk_areas: list[tuple[int, int]] = []
    m: int = len(grid)
    if not m:
        return global_flood_risk_areas
    
    n: int = len(grid[0])
    if not n:
        return global_flood_risk_areas
    
    return global_flood_risk_areas