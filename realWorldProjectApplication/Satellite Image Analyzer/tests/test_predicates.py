import unittest
from gridtools import predicates

class TestPredicates(unittest.TestCase):
    
    def setUp(self) -> None:
        self.grid_image = [
            [0, 1, 0],
            [1, 0, 1],
            [0, 1, 0]
        ]
        
        
        # Legend: 0 = land, 1 = water
        
    def test_is_within_bound(self):
        self.assertTrue(predicates.is_within_bound(0, 0, self.grid_image))
        self.assertTrue(predicates.is_within_bound(2, 2, self.grid_image))
        self.assertFalse(predicates.is_within_bound(-1, 0, self.grid_image))
        self.assertFalse(predicates.is_within_bound(3, 1, self.grid_image))
        self.assertFalse(predicates.is_within_bound(0, 3, self.grid_image))
        
    def test_is_water(self):
        self.assertTrue(predicates.is_water(0, 1, self.grid_image)) # water
        self.assertFalse(predicates.is_water(2, 0, self.grid_image)) # land
    
    def test_is_land(self):
        self.assertTrue(predicates.is_land(2, 2, self.grid_image)) # land
        self.assertFalse(predicates.is_land(0, 1, self.grid_image)) # water
        
    def test_is_edge_coord(self):
        self.assertTrue(predicates.is_edge_coord(0, 1, self.grid_image))  # top row
        self.assertTrue(predicates.is_edge_coord(2, 1, self.grid_image))  # bottom row
        self.assertTrue(predicates.is_edge_coord(1, 0, self.grid_image))  # left col
        self.assertTrue(predicates.is_edge_coord(1, 2, self.grid_image))  # right col
        self.assertFalse(predicates.is_edge_coord(1, 1, self.grid_image)) # interior
        
    def test_is_interior_coord(self):
        self.assertTrue(predicates.is_interior_coord(1, 1, self.grid_image)) # center
        self.assertFalse(predicates.is_interior_coord(0, 0, self.grid_image)) # edge
        self.assertFalse(predicates.is_interior_coord(2, 2, self.grid_image)) # edge

class TestPredicatesEmptyGrid(unittest.TestCase):
    def test_is_within_bound_on_empty_grid(self):
        grid = []
        self.assertFalse(predicates.is_within_bound(0, 0, grid))
        self.assertFalse(predicates.is_within_bound(-1, -1, grid))

    def test_is_within_bound_on_empty_row(self):
        grid = [[]]  # 1 row, 0 columns
        self.assertFalse(predicates.is_within_bound(0, 0, grid))
        self.assertFalse(predicates.is_within_bound(0, 1, grid))
        self.assertFalse(predicates.is_within_bound(1, 0, grid))

    def test_is_within_bound_out_of_range_on_nonempty(self):
        grid = [[0, 1], [1, 0]]
        self.assertFalse(predicates.is_within_bound(-1, 0, grid))
        self.assertFalse(predicates.is_within_bound(0, -1, grid))
        self.assertFalse(predicates.is_within_bound(2, 0, grid))
        self.assertFalse(predicates.is_within_bound(0, 2, grid))

    def test_is_within_bound_valid_on_nonempty(self):
        grid = [[0, 1], [1, 0]]
        self.assertTrue(predicates.is_within_bound(0, 0, grid))
        self.assertTrue(predicates.is_within_bound(1, 1, grid))