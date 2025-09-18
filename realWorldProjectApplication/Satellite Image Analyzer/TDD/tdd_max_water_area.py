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
        
    def test_grid_with_one_water_cell_return_one(self):
        grid = [
            [1]
        ]

        self.assertEqual(max_water_area(grid, neighbors_4),
                            1,
                            msg = f"expected 1 since grid contains one water cell"
                            )

        self.assertEqual(max_water_area(grid, neighbors_8),
                            1,
                            msg = f"expected 1 since grid contains one water cell"
                            )                   

    def test_uniformed_grid_with_all_water_cells(self):
        grid = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1],
        ]

        self.assertEqual(max_water_area(grid, neighbors_4),
                            9,
                            msg = f"expected 9 since grid contains nine water cells"
                            )

        self.assertEqual(max_water_area(grid, neighbors_8),
                            9,
                            msg = f"expected 1 since grid contains nine water cells"
                            )    

    def test_grid_with_mixed_cluster(self):
        grid = [
            [1, 1, 0],
            [1, 1, 0],
            [0, 0, 1],
            [1, 0, 0],
            [1, 1, 0],
        ]

        self.assertEqual(max_water_area(grid, neighbors_4),
                            4,
                            msg = f"expected 4 since grid does not traverse diagonally"
                            )

        self.assertEqual(max_water_area(grid, neighbors_8),
                            5,
                            msg = f"expected 5 since grid traverses diagonally"
                            )   
        
    def test_grid_with_disjoint_cluster(self):
        grid = [
            [1, 0, 1],
            [0, 0, 0],
            [1, 0, 1]
]

        self.assertEqual(max_water_area(grid, neighbors_4),
                            1,
                            msg = f"expected 1"
                            )

        self.assertEqual(max_water_area(grid, neighbors_8),
                            1,
                            msg = f"expected 1"
                            )          

    def test_grid_with_edge_cluster(self):
        grid = [
            [1, 1, 0, 0],
            [1, 0, 0, 1],
            [0, 0, 0, 1],
            [0, 1, 1, 1]
        ]

        self.assertEqual(max_water_area(grid, neighbors_4),
                            5,
                            msg = f"expected 5"
                            )

        self.assertEqual(max_water_area(grid, neighbors_8),
                            5,
                            msg = f"expected 5"
                            )    
        
    def test_grid_with_checkered_pattern(self):
        grid = [
            [1, 0, 1],
            [0, 1, 0],
            [1, 0, 1]
        ]

        self.assertEqual(max_water_area(grid, neighbors_4),
                            1,
                            msg = f"expected 5"
                            )

        self.assertEqual(max_water_area(grid, neighbors_8),
                            5,
                            msg = f"expected 5"
                            )            
                 