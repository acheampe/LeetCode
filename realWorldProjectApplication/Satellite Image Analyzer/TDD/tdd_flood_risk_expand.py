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
        