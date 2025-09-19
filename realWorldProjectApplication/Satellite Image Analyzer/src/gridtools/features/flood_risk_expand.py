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
    
    return []