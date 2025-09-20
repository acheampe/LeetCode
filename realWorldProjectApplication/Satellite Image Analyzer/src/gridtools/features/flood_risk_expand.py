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
    
    global_flood_risk_zones: list[tuple[int, int]] = []
    m: int = len(grid)
    
    if not m:
        print("not m")
        return global_flood_risk_zones
    
    n: int = len(grid[0])
    if not n:
        print("not n")
        return global_flood_risk_zones
    
    visited: set = set()
    marked_risk_zones: set = set()
    
    for i in range(m):
        for j in range(n):
            
            if (i, j) not in visited and is_water(i, j, grid):
                next_neighbor: list[tuple[int, int]] = neighbor_fn(i, j, grid)
                
                for r, c in next_neighbor:
                    
                    if (r, c) not in marked_risk_zones and is_land(r, c, grid):
                        global_flood_risk_zones.append((r, c))
                        marked_risk_zones.add((r, c))
                    
                    else:
                        visited.update((r, c))
                
    
    return global_flood_risk_zones