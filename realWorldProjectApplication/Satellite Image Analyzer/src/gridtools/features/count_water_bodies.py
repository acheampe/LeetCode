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
    
    marked_visited: set = set()
    body_count: int = 0
    
    # def is_water_body(r: int, c: int, accrued_body: list[tuple[int, int]]) -> list[tuple[int, int]]:
    #     """returns list"""
    #     pass
    
    
    
    return 0