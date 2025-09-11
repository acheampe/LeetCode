import pytest
from gridtools.predicates import (
    is_within_bound,
    is_water,
    is_land,
    is_edge_coord,
    is_interior_coord,
)

# ---------- is_within_bound ----------

@pytest.mark.parametrize(
    "grid,i,j,expected",
    [
        ([[0]], 0, 0, True),
        ([[0]], -1, 0, False),
        ([[0,1],[1,0]], 1, 1, True),
        ([[0,1],[1,0]], 2, 0, False),
        ([], 0, 0, False),              # empty grid
        ([[]], 0, 0, False),            # row but no cols
    ],
)
def test_is_within_bound(grid, i, j, expected):
    assert is_within_bound(i, j, grid) is expected


# ---------- is_land / is_water ----------
# (These assume you checked bounds first in calling code.)

@pytest.mark.parametrize(
    "grid,i,j",
    [
        ([[1,0]], 0, 1),        # grid[0][1] == 0
        ([[0],[0]], 1, 0),
    ],
)
def test_is_land_true(grid, i, j):
    assert is_land(i, j, grid) is True

@pytest.mark.parametrize(
    "grid,i,j",
    [
        ([[1,0]], 0, 0),
        ([[1],[0]], 0, 0),
    ],
)
def test_is_land_false(grid, i, j):
    assert is_land(i, j, grid) is False

@pytest.mark.parametrize(
    "grid,i,j",
    [
        ([[1,0]], 0, 0),        # grid[0][0] == 1
        ([[1],[1]], 1, 0),
    ],
)
def test_is_water_true(grid, i, j):
    assert is_water(i, j, grid) is True

@pytest.mark.parametrize(
    "grid,i,j",
    [
        ([[1,0]], 0, 1),
        ([[0],[1]], 0, 0),
    ],
)
def test_is_water_false(grid, i, j):
    assert is_water(i, j, grid) is False


# ---------- edges / interior ----------

@pytest.mark.parametrize(
    "grid,i,j,expected",
    [
        ([[0,0],[0,0]], 0, 0, True),   # top-left corner
        ([[0,0],[0,0]], 1, 1, True),   # bottom-right corner
        ([[0,0,0]], 0, 1, True),       # top row
        ([[0],[0],[0]], 1, 0, True),   # left col
        ([[0,0],[0,0]], 0, 1, True),
        ([[0,0],[0,0]], 1, 0, True),
        ([[0,0],[0,0]], 0, 0, True),
    ],
)
def test_is_edge_coord_true(grid, i, j, expected):
    assert is_edge_coord(i, j, grid) is expected

@pytest.mark.parametrize(
    "grid,i,j,expected",
    [
        ([[0,0,0],[0,0,0],[0,0,0]], 1, 1, False),  # center
    ],
)
def test_is_edge_coord_false(grid, i, j, expected):
    assert is_edge_coord(i, j, grid) is expected


@pytest.mark.parametrize(
    "grid,i,j,expected",
    [
        ([[0,0,0],[0,0,0],[0,0,0]], 1, 1, True),   # center
        ([[0,0],[0,0]], 0, 0, False),              # corner
        ([[0,0],[0,0]], 0, 1, False),              # edge
        ([[0,0],[0,0]], 1, 0, False),              # edge
        ([[0,0],[0,0]], 1, 1, False),              # corner
    ],
)
def test_is_interior_coord(grid, i, j, expected):
    assert is_interior_coord(i, j, grid) is expected