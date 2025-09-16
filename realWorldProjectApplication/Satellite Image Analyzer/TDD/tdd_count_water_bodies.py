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

        self.complex_gridv2 = [
            [1, 1, 0, 1],
            [0, 0, 1, 0],
            [0, 1, 1, 0],
            [1, 0, 1, 0],
            [0, 0, 0, 0],
            [1, 1, 0, 0]
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

    def test_uniformed_grid_return_4_with_neighbors_4(self):
        expected: int = 4
        result: int = count_water_bodies(self.complex_grid, neighbors_4)
        self.assertEqual(result, expected, 
                            msg=f"Amount of bodies of water returned {result}, expected {expected}"
                            )

    def test_uniformed_grid_return_1_with_neighbors_8(self):
        expected: int = 1
        result: int = count_water_bodies(self.complex_grid, neighbors_8)
        self.assertEqual(result, expected, 
                            msg=f"Amount of bodies of water returned {result}, expected {expected}"
                            )  

    def test_uniformed_grid_return_2_with_neighbors_8(self):
        expected: int = 2
        result: int = count_water_bodies(self.complex_gridv2, neighbors_8)
        self.assertEqual(result, expected, 
                            msg=f"Amount of bodies of water returned {result}, expected {expected}"
                            )     