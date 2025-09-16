import unittest

from gridtools.features.count_water_bodies import count_water_bodies

from gridtools.connectivity import (
    neighbors_4,
    neighbors_8,
)

class TestCountWaterBodies(unittest.TestCase):
    
    def setUp(self) -> None:
        
        # Legends: 1 = water, 0 = land
        self.uniformed_grid = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1],
        ]
        
        self.complex_grid = [
            [1, 1, 0, 1],
            [0, 0, 1, 0],
            [0, 1, 1, 0],
            [1, 0, 1, 0]
        ]
        
        self.empty_grid = [
            []
        ]
        
    def test_empty_grid_returns_zero_with_neighbors_4(self):
        expected: int = 0
        result: int = count_water_bodies(self.empty_grid, neighbors_4)
        self.assertEqual(result, expected, 
                            msg=f"Amount of bodies of water returned {result}, expected {expected}"
                            )

    def test_empty_grid_returns_zero_with_neighbors_8(self):
        expected: int = 0
        result: int = count_water_bodies(self.empty_grid, neighbors_8)
        self.assertEqual(result, expected, 
                            msg=f"Amount of bodies of water returned {result}, expected {expected}"
                            )
    
    def test_uniformed_grid_return_one_with_neighbors_4(self):
        expected: int = 1
        result: int = count_water_bodies(self.uniformed_grid, neighbors_4)
        self.assertEqual(result, expected, 
                            msg=f"Amount of bodies of water returned {result}, expected {expected}"
                            )
    
    def test_uniformed_grid_return_one_with_neighbors_8(self):
        expected: int = 1
        result: int = count_water_bodies(self.uniformed_grid, neighbors_8)
        self.assertEqual(result, expected, 
                            msg=f"Amount of bodies of water returned {result}, expected {expected}"
                            )