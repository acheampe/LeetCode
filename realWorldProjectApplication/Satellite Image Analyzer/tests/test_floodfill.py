import unittest
from gridtools.floodfill import floodfill
from gridtools.connectivity import neighbors_4, neighbors_8

class TestFloodfillBlackBox(unittest.TestCase):
    def setUp(self):
        self.grid1 = []  # empty
        self.grid2 = [[0,0],[0,0]]  # all land
        self.grid3 = [[1]]  # single water
        self.grid4 = [[1,1],[1,1]]  # 2x2 water
        self.grid5 = [[1,0],[0,1]]  # diagonal only
        self.grid6 = [
            [1,0,1],
            [0,0,0],
            [1,1,0]
        ]  # disjoint regions

    def test_empty_grid(self):
        self.assertEqual(floodfill(0, 0, self.grid1, neighbors_4), [])

    def test_starting_on_land(self):
        self.assertEqual(floodfill(0, 0, self.grid2, neighbors_4), [])

    def test_single_water_cell(self):
        result = floodfill(0, 0, self.grid3, neighbors_4)
        self.assertCountEqual(result, [(0, 0)])

    def test_square_water_block(self):
        result = floodfill(0, 0, self.grid4, neighbors_4)
        expected = [(0,0),(0,1),(1,0),(1,1)]
        self.assertCountEqual(result, expected)

    def test_diagonal_neighbors_with_8(self):
        result = floodfill(0, 0, self.grid5, neighbors_8)
        expected = [(0,0),(1,1)]
        self.assertCountEqual(result, expected)

    def test_disjoint_regions(self):
        result = floodfill(0, 0, self.grid6, neighbors_4)
        self.assertCountEqual(result, [(0,0)])  # only top-left

        result2 = floodfill(2, 0, self.grid6, neighbors_4)
        self.assertCountEqual(result2, [(2,0),(2,1)])  # bottom cluster