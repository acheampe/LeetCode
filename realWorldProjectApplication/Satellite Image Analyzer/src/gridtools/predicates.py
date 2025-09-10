# file maintains bool definition for code 

def is_within_bound(i: int, j: int, grid_image: list[list[int]]) -> bool:
    
    if not grid_image or not grid_image[0]:
        return False
    
    m, n = len(grid_image), len(grid_image[0])
    return ((0 <= i < m) and (0 <= j < n))

# must check bounds first within main logic of code
def is_water(i: int, j: int, grid_image: list[list[int]]) -> bool: 
    return grid_image[i][j] == 1 # 1 defines water

# must check bounds first within main logic of code
def is_land(i: int, j: int, grid_image: list[list[int]]) -> bool: 
    return grid_image[i][j] == 0 # 0 defines land

# must check bounds first within main logic of code
def is_edge_coord(i: int, j: int, grid_image: list[list[int]]) -> bool:
    m, n = len(grid_image), len(grid_image[0])
    return ((0 == i) or (i == (m - 1)) or (0 == j) or (j == (n - 1)))

# must check bounds first within main logic of code
def is_interior_coord(i: int, j: int, grid_image: list[list[int]]) -> bool:
    m, n = len(grid_image), len(grid_image[0])
    return ((0 < i < (m - 1)) and (0 < j < (n - 1)))