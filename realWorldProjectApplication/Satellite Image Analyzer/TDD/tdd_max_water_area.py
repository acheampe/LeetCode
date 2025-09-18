import unittest

from gridtools.features.max_water_area import max_water_area

from gridtools.connectivity import (
    neighbors_4,
    neighbors_8,
)

class TestMaxWaterBodies(unittest.TestCase):
    
    # Legends: 1 = water, 0 = land
    def test_empty_grid_return_zero(self):
        grid = []

        self.assertEqual(max_water_area(grid, neighbors_4),
                            0,
                            msg = f"expected 0 since grid is empty"
                            )

        self.assertEqual(max_water_area(grid, neighbors_8),
                            0,
                            msg = f"expected 0 since grid is empty"
                            ) 
        
    def test_empty_nested_grid_return_zero(self):
        grid = [
            []
        ]

        self.assertEqual(max_water_area(grid, neighbors_4),
                            0,
                            msg = f"expected 0 since nested grid is empty"
                            )

        self.assertEqual(max_water_area(grid, neighbors_8),
                            0,
                            msg = f"expected 0 since nested grid is empty"
                            )
    
    def test_one_land_cell_return_zero(self):
        grid = [
            [0]
        ]

        self.assertEqual(max_water_area(grid, neighbors_4),
                            0,
                            msg = f"expected 0 since grid only contains land"
                            )

        self.assertEqual(max_water_area(grid, neighbors_8),
                            0,
                            msg = f"expected 0 since grid only contains land"
                            ) 
        
                  
              