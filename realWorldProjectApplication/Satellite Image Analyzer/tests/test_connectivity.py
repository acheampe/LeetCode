import unittest
from gridtools.connectivity import neighbors_4, neighbors_8

class TestNeighbors(unittest.TestCase):

    def setUp(self):
        # Simple 3x3 grid so we can test corners, edges, center
        self.grid = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]

    def test_neighbors_4_matrix(self):
        # Format: (i, j): expected_neighbors
        cases = {
            (1, 1): [(0, 1), (2, 1), (1, 0), (1, 2)],  # center
            (0, 0): [(0, 1), (1, 0)],                  # top-left corner
            (0, 2): [(0, 1), (1, 2)],                  # top-right corner
            (2, 0): [(1, 0), (2, 1)],                  # bottom-left corner
            (2, 2): [(1, 2), (2, 1)],                  # bottom-right corner
            (0, 1): [(0, 0), (0, 2), (1, 1)],          # top edge
            (1, 0): [(0, 0), (2, 0), (1, 1)],          # left edge
            (1, 2): [(0, 2), (2, 2), (1, 1)],          # right edge
            (2, 1): [(2, 0), (2, 2), (1, 1)],          # bottom edge
        }

        for (i, j), expected in cases.items():
            result = neighbors_4(i, j, self.grid)
            self.assertCountEqual(
                result, expected,
                msg=f"neighbors_4({i},{j}) returned {result}, expected {expected}"
            )

    def test_neighbors_8_matrix(self):
        # Format: (i, j): expected_neighbors
        cases = {
            (1, 1): [  # center has 8 neighbors
                (0, 0), (0, 1), (0, 2),
                (1, 0),        (1, 2),
                (2, 0), (2, 1), (2, 2),
            ],
            (0, 0): [(0, 1), (1, 0), (1, 1)],           # top-left corner
            (0, 2): [(0, 1), (1, 2), (1, 1)],           # top-right corner
            (2, 0): [(1, 0), (2, 1), (1, 1)],           # bottom-left corner
            (2, 2): [(1, 2), (2, 1), (1, 1)],           # bottom-right corner
            (0, 1): [(0, 0), (0, 2), (1, 0), (1, 1), (1, 2)],   # top edge
            (1, 0): [(0, 0), (2, 0), (0, 1), (1, 1), (2, 1)],   # left edge
            (1, 2): [(0, 2), (2, 2), (0, 1), (1, 1), (2, 1)],   # right edge
            (2, 1): [(2, 0), (2, 2), (1, 0), (1, 1), (1, 2)],   # bottom edge
        }

        for (i, j), expected in cases.items():
            result = neighbors_8(i, j, self.grid)
            self.assertCountEqual(
                result, expected,
                msg=f"neighbors_8({i},{j}) returned {result}, expected {expected}"
            )


if __name__ == "__main__":
    unittest.main()