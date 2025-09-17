import unittest

from gridtools.features.count_enclosed_lakes import count_enclosed_lakes
from gridtools.connectivity import neighbors_4, neighbors_8


class TestCountEnclosedLakesBlackBox(unittest.TestCase):

    def test_empty_grid(self):
        self.assertEqual(
            count_enclosed_lakes([], neighbors_4), 0,
            "Empty grid should return 0 enclosed lakes"
        )
        self.assertEqual(
            count_enclosed_lakes([[]], neighbors_8), 0,
            "Empty nested grid should return 0 enclosed lakes"
        )

    def test_uniform_grid_all_water(self):
        grid = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1],
        ]
        self.assertEqual(
            count_enclosed_lakes(grid, neighbors_4), 0,
            "All-water grid should have no enclosed lakes"
        )

    def test_no_enclosed_lakes(self):
        grid = [
            [1, 1, 0, 1],
            [0, 0, 1, 0],
            [0, 1, 1, 0],
            [1, 0, 1, 0]
        ]
        self.assertEqual(
            count_enclosed_lakes(grid, neighbors_4), 0,
            "This grid has no enclosed lakes under 4-neighbors"
        )
        self.assertEqual(
            count_enclosed_lakes(grid, neighbors_8), 0,
            "This grid has no enclosed lakes under 8-neighbors"
        )

    def test_one_enclosed_lake(self):
        grid = [
            [1, 1, 0, 1],
            [0, 0, 1, 0],
            [0, 1, 1, 0],
            [1, 0, 1, 0],
            [0, 0, 0, 0],
            [1, 1, 0, 0]
        ]
        self.assertEqual(
            count_enclosed_lakes(grid, neighbors_4), 1,
            "Should detect one enclosed lake with 4-neighbors"
        )
        self.assertEqual(
            count_enclosed_lakes(grid, neighbors_8), 0,
            "Should detect no enclosed lakes with 8-neighbors"
        )

    def test_multiple_enclosed_lakes(self):
        grid = [
            [1, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0],
            [0, 1, 1, 0, 0, 1, 1, 0],
            [1, 0, 1, 0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 1, 1, 0, 0]
        ]
        self.assertEqual(
            count_enclosed_lakes(grid, neighbors_4), 3,
            "Should detect three enclosed lakes with 4-neighbors"
        )
        self.assertEqual(
            count_enclosed_lakes(grid, neighbors_8), 2,
            "Should detect two enclosed lakes with 8-neighbors"
        )


if __name__ == "__main__":
    unittest.main()