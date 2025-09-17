import unittest

from gridtools.features.count_enclosed_lakes import count_enclosed_lakes
from gridtools.connectivity import neighbors_4, neighbors_8


class TestCountEnclosedLakesBlackBox(unittest.TestCase):

    def test_single_cell_water_on_border(self):
        grid = [
            [1]
        ]
        self.assertEqual(
            count_enclosed_lakes(grid, neighbors_4), 0,
            "Single border cell of water should not be counted as enclosed"
        )

    def test_single_cell_water_interior(self):
        grid = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0],
        ]
        self.assertEqual(
            count_enclosed_lakes(grid, neighbors_4), 1,
            "Single interior water cell should be enclosed under 4-neighbors"
        )
        self.assertEqual(
            count_enclosed_lakes(grid, neighbors_8), 1,
            "Single interior water cell should also be enclosed under 8-neighbors"
        )

    def test_ring_of_land_with_water_center(self):
        grid = [
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 1, 0, 1, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0],
        ]
        self.assertEqual(
            count_enclosed_lakes(grid, neighbors_4), 1,
            "The 3x3 block of water in the center is enclosed"
        )
        self.assertEqual(
            count_enclosed_lakes(grid, neighbors_8), 1,
            "Still enclosed even with 8-neighbors"
        )

    def test_diagonal_connection_breaks_enclosure_neighbors_8(self):
        grid = [
            [0, 1, 0],
            [1, 0, 1],
            [0, 1, 0],
        ]
        self.assertEqual(
            count_enclosed_lakes(grid, neighbors_4), 4,
            "4-neighbors sees four isolated water cells"
        )
        self.assertEqual(
            count_enclosed_lakes(grid, neighbors_8), 1,
            "8-neighbors connects diagonals, so only one enclosed lake"
        )

    def test_multiple_small_enclosed_pools(self):
        grid = [
            [0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0],
        ]
        self.assertEqual(
            count_enclosed_lakes(grid, neighbors_4), 4,
            "Each isolated interior water cell is its own enclosed pool under 4-neighbors"
        )
        self.assertEqual(
            count_enclosed_lakes(grid, neighbors_8), 4,
            "Same result for 8-neighbors since cells are not diagonally adjacent"
        )


if __name__ == "__main__":
    unittest.main()