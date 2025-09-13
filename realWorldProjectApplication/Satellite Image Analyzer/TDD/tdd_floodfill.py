import unittest

from gridtools.floodfill import (
    floodfill,
)

class TestFloodfill(unittest.TestCase):
    
    def setUp(self) -> None:
        
        self.grid = [
            [1, 1, 0],
            [1, 0, 1],
            [0, 1, 0]
        ]
        
        # Legend: 0 = land, 1 = water
        
    def test_floodfill_returns_empty_on_land_cell(self):
        expected: list[tuple[int, int]] = []
        result = floodfill(1, 1, self.grid)
        self.assertEqual(result, 
                            expected, 
                            msg=f"floodfill_water for (1, 1) returned {result}, expected {expected}")
        
        
