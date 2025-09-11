from gridtools.predicates import is_within_bound
# file defining valid neighbor pattern

directions_4 = [(0, -1), (0, 1), (-1, 0), (1, 0)]
# returns valid neighbor in up, down, left, right directions
def neighbors_4(i: int, j: int, grid: list[list[int]]) -> list[tuple[int, int]]:
    valid_nei = []
    for dr, dc in directions_4:
        nr, nc = dr + i, dc + j
        if is_within_bound(nr, nc, grid):
            valid_nei.append((nr, nc))
    return valid_nei
    
# def neighbors_8(i: int, j: int, grid: list[list[int]]) -> list[tuple[int, int]]:
#     return 0