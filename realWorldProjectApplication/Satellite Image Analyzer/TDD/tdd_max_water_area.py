import unittest

from gridtools.features.max_water_area import max_water_area

from gridtools.connectivity import (
    neighbors_4,
    neighbors_8,
)

class TestMaxWaterBodies(unittest.TestCase):
    
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