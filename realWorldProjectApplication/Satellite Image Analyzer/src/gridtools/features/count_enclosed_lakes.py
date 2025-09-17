from gridtools.predicates import (
    is_water, 
    is_interior_coord,
    is_edge_coord
)

from gridtools.floodfill import (
    NeighborFn,
    floodfill
)

def count_enclosed_lakes(grid: list[list[int]], neighbor_fn: NeighborFn) -> int:
    """_summary_

    Args:
        grid (list[list[int]]): Count distinct lake bodies (connected groups of 1s) that 
        does not touch edges of grid, using the given neighbor function.
        
    Returns:
        int: returns the amount of separate lakes provided in image
    """
    
    count_enclosed: int= 0
    m: int = len(grid)
    
    if not m:
        return count_enclosed # will be zero at this point
    
    n: int = len(grid[0])
    
    if not n:
        return count_enclosed # will be zero at this point 
    
    visited: set[tuple[int, int]] = set()
    
    for i in range(m):
        for j in range(n):
            if (i, j) not in visited and is_water(i, j, grid) and is_interior_coord(i, j, grid):
                region = floodfill(i, j, grid, neighbor_fn)
                visited.update(region)
                
                while region:
                    r, c = region.pop()
                    if is_edge_coord(r, c, grid):
                        break # wonder if this is appropriate way to handle a production level loop
                
                else:
                    count_enclosed += 1
                        
    return count_enclosed