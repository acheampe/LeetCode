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
    
    visited: set = set()
    
    for i in range(m):
        for j in range(n):
            
            if (i, j) not in visited and is_water(i, j, grid):
                region = floodfill(i, j, grid, neighbor_fn)
                
                for r, c in region:
                    
                    if is_land(r, c, grid):
                        global_flood_risk_areas.append((r, c)) 
                    
                    else:
                        visited.update((r, c))
                
    
    return global_flood_risk_areas