from gridtools.predicates import is_within_bound
# file defining valid neighbor pattern

directions_4 = [(0, -1), (0, 1), (-1, 0), (1, 0)]
directions_8 = [
    (0, -1), (0, 1), (-1, 0), (1, 0),
    (1, -1), (-1, -1), (1, 1), (-1, 1)  
]
# returns valid neighbor in up, down, left, right directions
def neighbors(i: int, j: int, grid: list[list[int]], directions: list[tuple[int, int]]):
    return [
        (i + dr, j + dc)
        for dr, dc in directions
        if is_within_bound(i + dr, j + dc, grid)
    ]
    
def neighbors_4(i: int, j: int, grid: list[list[int]]) -> list[tuple[int, int]]:
    return neighbors(i, j, grid, directions_4)

def neighbors_8(i: int, j: int, grid: list[list[int]]) -> list[tuple[int, int]]:
    return neighbors(i, j, grid, directions_8)