import unittest

from gridtools.features.flood_risk_expand import flood_risk_expand

from gridtools.connectivity import (
    neighbors_4,
    neighbors_8,
)

class TestFloodRiskExpand(unittest.TestCase):
    
    def test_empty_grid(self):
        grid: list[list[int]] = []
        expected: list[tuple[int, int]] = []
        
        self.assertEqual(flood_risk_expand(grid, neighbors_4), expected,
                                           msg=f"Empty Grid Should return 0"
                                           )
        
        self.assertEqual(flood_risk_expand(grid, neighbors_8), expected,
                                           msg=f"Empty Grid Should return 0"
                                           )
    
    def test_single_cell_water_grid(self):
        grid: list[list[int]] = [[1]]
        expected: list[tuple[int, int]] = []
    
        self.assertEqual(expected, flood_risk_expand(grid, neighbors_4), 
                         msg=f"expected {expected}, no neighbors in grid")

        self.assertEqual(expected, flood_risk_expand(grid, neighbors_8), 
                         msg=f"expected {expected}, no neighbors in grid") 
        
              
    def test_single_cell_land_grid(self):
        grid: list[list[int]] = [[0]]
        expected: list[tuple[int, int]] = []
    
        self.assertEqual(expected, flood_risk_expand(grid, neighbors_4), 
                         msg=f"expected {expected}, no valid water cell in grid")     
        
        self.assertEqual(expected, flood_risk_expand(grid, neighbors_8), 
                         msg=f"expected {expected}, no valid water cell in grid")    

    def test_one_flood_risk_cell(self):
        grid: list[list[int]] = [[0, 1]]
        expected: list[tuple[int, int]] = [(0, 0)]
       
        nei_4_return = flood_risk_expand(grid, neighbors_4)
        self.assertEqual(expected, nei_4_return, 
                         msg=f"expected {expected}, returned {nei_4_return}")     
        
        nei_8_return = flood_risk_expand(grid, neighbors_8)
        self.assertEqual(expected, nei_8_return, 
                         msg=f"expected {expected}, returned {nei_8_return}")   

    def test_two_flood_risk_cell(self):
        grid: list[list[int]] = [[0, 1],
                                 [1, 0]
                                 ]
        expected: list[tuple[int, int]] = [(0, 0), (1, 1)]
       
        nei_4_return = flood_risk_expand(grid, neighbors_4)
        self.assertCountEqual(expected, nei_4_return, 
                         msg=f"expected {expected}, returned {nei_4_return}")     
        
        nei_8_return = flood_risk_expand(grid, neighbors_8)
        self.assertCountEqual(expected, nei_8_return, 
                         msg=f"expected {expected}, returned {nei_8_return}")
        
    def test_uniformed_water_cells(self):
        grid: list[list[int]] = [[1, 1, 1],
                                 [1, 1, 1],
                                 [1, 1, 1]
                                 ]
        expected: list[tuple[int, int]] = []
       
        nei_4_return = flood_risk_expand(grid, neighbors_4)
        self.assertCountEqual(expected, nei_4_return, 
                         msg=f"expected {expected}, returned {nei_4_return}")     
        
        nei_8_return = flood_risk_expand(grid, neighbors_8)
        self.assertCountEqual(expected, nei_8_return, 
                         msg=f"expected {expected}, returned {nei_8_return}")

    def test_uniformed_land_cells(self):
        grid: list[list[int]] = [[0, 0, 0],
                                 [0, 0, 0],
                                 [0, 0, 0]
                                 ]
        expected: list[tuple[int, int]] = []
       
        nei_4_return = flood_risk_expand(grid, neighbors_4)
        self.assertCountEqual(expected, nei_4_return, 
                         msg=f"expected {expected}, returned {nei_4_return}")     
        
        nei_8_return = flood_risk_expand(grid, neighbors_8)
        self.assertCountEqual(expected, nei_8_return, 
                         msg=f"expected {expected}, returned {nei_8_return}")               