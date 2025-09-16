import unittest

from gridtools.features.count_water_bodies import count_water_bodies
from gridtools.connectivity import neighbors_4, neighbors_8


class TestCountWaterBodiesBlackBox(unittest.TestCase):

    def test_empty_grid(self):
        grid = [[]]
        expected = 0
        result = count_water_bodies(grid, neighbors_4)
        self.assertEqual(result, expected)

    def test_no_water(self):
        grid = [
            [0, 0],
            [0, 0]
        ]
        expected = 0
        result = count_water_bodies(grid, neighbors_4)
        self.assertEqual(result, expected)

    def test_all_water(self):
        grid = [
            [1, 1],
            [1, 1]
        ]
        expected = 1
        result = count_water_bodies(grid, neighbors_4)
        self.assertEqual(result, expected)

    def test_two_disconnected_bodies(self):
        grid = [
            [1, 0],
            [0, 1]
        ]
        expected = 2
        result = count_water_bodies(grid, neighbors_4)
        self.assertEqual(result, expected)

    def test_diagonal_connected_neighbors_4(self):
        grid = [
            [1, 0],
            [0, 1]
        ]
        # with neighbors_4 diagonals don’t connect
        expected = 2
        result = count_water_bodies(grid, neighbors_4)
        self.assertEqual(result, expected)

    def test_diagonal_connected_neighbors_8(self):
        grid = [
            [1, 0],
            [0, 1]
        ]
        # with neighbors_8 diagonals connect, so one body
        expected = 1
        result = count_water_bodies(grid, neighbors_8)
        self.assertEqual(result, expected)

    def test_complex_case_neighbors_4(self):
        grid = [
            [1, 1, 0, 1],
            [0, 0, 1, 0],
            [0, 1, 1, 0],
            [1, 0, 1, 0]
        ]
        # manual counting with 4-neighbors: 4 water bodies
        expected = 4
        result = count_water_bodies(grid, neighbors_4)
        self.assertEqual(result, expected)

    def test_complex_case_neighbors_8(self):
        grid = [
            [1, 1, 0, 1],
            [0, 0, 1, 0],
            [0, 1, 1, 0],
            [1, 0, 1, 0]
        ]
        # manual counting with 8-neighbors: fewer groups (diagonals connect)
        expected = 2
        result = count_water_bodies(grid, neighbors_8)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()