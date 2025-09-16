from gridtools.floodfill import floodfill

def count_water_bodies(i: int, j: int, grid: list[list[int]]) -> int:
    """_summary_

    Args:
        i (int): row number of grid coordinate
        j (int): col number of grid coordinate
        grid (list[list[int]]): grid image to analyze count_water bodies

    Returns:
        int: returns the amount of separate bodies of water provides in image
    """
    
    return 0