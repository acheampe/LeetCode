import unittest

from gridtools.connectivity import (
    neighbors_4,
    # neighbors_8,
)

class TestConnectivity(unittest.TestCase):
    
    def setUp(self) -> None:
        self.grid = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]
        
    def test_neighbors_4_center(self):
        
        # nei of (1, 1), should be up, down, left, right
        expected = [(0, 1), (2, 1), (1, 0), (1,2)]
        result = neighbors_4(1, 1, self.grid)
        self.assertCountEqual(result, expected, msg=f"neighbors_4 for center (1, 1) returned {result}, expected {expected}")
        
    def test_neighbors_4_top_left(self):
        # test coord: (0, 0)
        expected = [(0, 1), (1, 0)]
        result = neighbors_4(0, 0, self.grid)
        self.assertCountEqual(result, expected, msg=f"neighbors_4 for top left (0, 0) returned {result}, expected {expected}")
