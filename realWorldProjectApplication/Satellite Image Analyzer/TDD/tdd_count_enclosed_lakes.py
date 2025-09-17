import unittest

from gridtools.features.count_enclosed_lakes import count_enclosed_lakes

from gridtools.connectivity import (
    neighbors_4,
    neighbors_8,
)
class TestCountEnclosedLakes(unittest.TestCase):
    
    def setUp(self) -> None:
        
        # Legends: 1 = water, 0 = land
        self.empty_grid = []
        
        self.empty_nested_grid = [
            []
            ]
        
        self.cornered_water_grid = [
                [1,0,1],
                [0,0,0],
                [1,0,1],
        ]
        self.uniformed_grid = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1],
        ]

        self.complex_grid_no_enclosed = [
            [1, 1, 0, 1],
            [0, 0, 1, 0],
            [0, 1, 1, 0],
            [1, 0, 1, 0],
        ]

        # no enclosed for neighbor_8, 1 enclosed for neighbor_4
        self.complex_gridv2 = [
            [1, 1, 0, 1],
            [0, 0, 1, 0],
            [0, 1, 1, 0],
            [1, 0, 1, 0],
            [0, 0, 0, 0],
            [1, 1, 0, 0],
        ]

        # 3 enclosed for neighbor_4, 2 enclosed for neighbor_8
        self.complex_gridv3 = [
            [1, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0],
            [0, 1, 1, 0, 0, 1, 1, 0],
            [1, 0, 1, 0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 1, 1, 0, 0],
        ]
    
    def test_empty_grid_return_zero_nei_4(self):
        expected: int = 0
        returned: int = count_enclosed_lakes(self.empty_grid, neighbors_4)
        
        self.assertEqual(expected,
                         returned,
                         msg=f"expected {expected} but returned {returned}"
                         )

    def test_empty_grid_return_zero_nei_8(self):
        expected: int = 0
        returned: int = count_enclosed_lakes(self.empty_grid, neighbors_8)
        
        self.assertEqual(expected,
                         returned,
                         msg=f"expected {expected} but returned {returned}"
                         )

    def test_empty_nested_grid_return_zero_nei_4(self):
        expected: int = 0
        returned: int = count_enclosed_lakes(self.empty_nested_grid, neighbors_4)
        
        self.assertEqual(expected,
                         returned,
                         msg=f"expected {expected} but returned {returned}"
                         )

    def test_empty_nested_grid_return_zero_nei_8(self):
        expected: int = 0
        returned: int = count_enclosed_lakes(self.empty_nested_grid, neighbors_8)
        
        self.assertEqual(expected,
                         returned,
                         msg=f"expected {expected} but returned {returned}"
                         )

    def test_uniformed_grid_return_zero_nei_4(self):
        expected: int = 0
        returned: int = count_enclosed_lakes(self.empty_nested_grid, neighbors_4)
        
        self.assertEqual(expected,
                         returned,
                         msg=f"expected {expected} but returned {returned}"
                         )
        
    def test_uniformed_grid_return_zero_nei_8(self):
        expected: int = 0
        returned: int = count_enclosed_lakes(self.empty_nested_grid, neighbors_8)
        
        self.assertEqual(expected,
                         returned,
                         msg=f"expected {expected} but returned {returned}"
                         )  
 
    def test_complex_grid_no_enclosed_zero_nei_4(self):
        expected: int = 0
        returned: int = count_enclosed_lakes(self.empty_nested_grid, neighbors_4)
        
        self.assertEqual(expected,
                         returned,
                         msg=f"expected {expected} but returned {returned}"
                         )  
    
    def test_complex_grid_no_enclosed_return_zero_nei_8(self):
        expected: int = 0
        returned: int = count_enclosed_lakes(self.empty_nested_grid, neighbors_8)
        
        self.assertEqual(expected,
                            returned,
                            msg=f"expected {expected} but returned {returned}"
                            )
        
    def test_complex_gridv2_return_one_nei_4(self):
        expected: int = 1
        returned: int = count_enclosed_lakes(self.complex_gridv2, neighbors_4)
        
        self.assertEqual(expected,
                            returned,
                            msg=f"expected {expected} but returned {returned}"
                            )  
        
    def test_complex_gridv2_return_zero_nei_8(self):
        expected: int = 0
        returned: int = count_enclosed_lakes(self.complex_gridv2, neighbors_8)
        
        self.assertEqual(expected,
                            returned,
                            msg=f"expected {expected} but returned {returned}"
                            )              
        
    def test_complex_gridv3_return_one_nei_4(self):
        expected: int = 2
        returned: int = count_enclosed_lakes(self.complex_gridv3, neighbors_4)
        
        self.assertEqual(expected,
                            returned,
                            msg=f"expected {expected} but returned {returned}"
                            )  