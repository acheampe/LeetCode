import unittest

from gridtools.floodfill import (
    floodfill,
    # landfill
)

class TestFloodfill(unittest.TestCase):
    
    def setUp(self) -> None:
        
        self.grid = [
            [1, 1, 0, 0],
            [1, 0, 0, 1],
            [0, 1, 0, 0],
            [0, 0, 1, 1],
            [1, 0, 0, 0],
            [0, 1, 0, 0]
        ]
        
        # Legend: 0 = land, 1 = water
        
    def test_floodfill_returns_empty_on_land_cell(self):
        expected: list[tuple[int, int]] = []
        result = floodfill(1, 1, self.grid)
        self.assertEqual(result, 
                            expected, 
                            msg=f"floodfill for (1, 1) returned {result}, expected {expected}")
        
    def test_out_of_bound_floodfill(self):
        expected: list[tuple[int, int]] = []
        result = floodfill(10, 10, self.grid)
        self.assertEqual(result, 
                            expected, 
                            msg=f"floodfill for (10, 10) returned {result}, expected {expected}")
            
    def test_isolated_water_cell(self):
        expected: list[tuple[int, int]] = [(1, 3)]
        result = floodfill(1, 3, self.grid)
        self.assertEqual(result, 
                            expected, 
                            msg=f"floodfill for (1, 3) returned {result}, expected {expected}")

    def test_two_adjacent_water_cells_neigh_4(self):
        expected: list[tuple[int, int]] = [(3, 2), (3, 3)]
        result = floodfill(3, 3, self.grid)
        self.assertCountEqual(result, 
                            expected, 
                            msg=f"floodfill for (3, 3) returned {result}, expected {expected}")

    def test_two_diag_water_cells_neigh_8(self):
        expected: list[tuple[int, int]] = [(5, 1), (4, 0)]
        result = floodfill(5, 1, self.grid)
        self.assertCountEqual(result, 
                            expected, 
                            msg=f"floodfill for (5, 1) returned {result}, expected {expected}")
                                   