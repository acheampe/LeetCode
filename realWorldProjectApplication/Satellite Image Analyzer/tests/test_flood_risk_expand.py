import unittest

from gridtools.features.flood_risk_expand import flood_risk_expand
from gridtools.connectivity import neighbors_4, neighbors_8


class TestFloodRiskExpandBlackBox(unittest.TestCase):

    def test_empty_grid_returns_empty_list(self):
        grid = []
        expected = []
        self.assertEqual(
            flood_risk_expand(grid, neighbors_4),
            expected,
            "Empty grid should return []"
        )

    def test_empty_nested_grid(self):
        grid = [[]]
        expected = []
        result = flood_risk_expand(grid, neighbors_4)
        self.assertEqual(result, expected,
                        msg=f"Empty nested grid should return {expected}")
        
    def test_skip_already_visited_water_cell(self):
        grid = [
            [1, 1],
            [0, 0]
        ]
        # Both water cells touch the same land cells (0,0) and (0,1)
        result = flood_risk_expand(grid, neighbors_4)
        expected = [(1,0), (1,1)]  # land directly below water row
        self.assertCountEqual(result, expected)
        
    def test_single_water_in_corner(self):
        grid = [
            [1, 0],
            [0, 0],
        ]
        # For 4-neighbors: flood risk = [(0,1), (1,0)]
        expected_4 = [(0,1), (1,0)]
        result_4 = flood_risk_expand(grid, neighbors_4)
        self.assertCountEqual(result_4, expected_4,
                              msg=f"Expected {expected_4}, got {result_4} (4-neighbors)")

        # For 8-neighbors: add diagonals, so also (1,1)
        expected_8 = [(0,1), (1,0), (1,1)]
        result_8 = flood_risk_expand(grid, neighbors_8)
        self.assertCountEqual(result_8, expected_8,
                              msg=f"Expected {expected_8}, got {result_8} (8-neighbors)")

    def test_all_land_no_risk(self):
        grid = [
            [0, 0],
            [0, 0],
        ]
        self.assertEqual(flood_risk_expand(grid, neighbors_4), [],
                         "All-land grid should return empty risk list (4-neighbors)")
        self.assertEqual(flood_risk_expand(grid, neighbors_8), [],
                         "All-land grid should return empty risk list (8-neighbors)")

    def test_full_water_grid(self):
        grid = [
            [1, 1],
            [1, 1],
        ]
        # No adjacent land exists, so risk zones = []
        self.assertEqual(flood_risk_expand(grid, neighbors_4), [],
                         "Full water grid should return empty risk list (4-neighbors)")
        self.assertEqual(flood_risk_expand(grid, neighbors_8), [],
                         "Full water grid should return empty risk list (8-neighbors)")

    def test_water_cross_shape(self):
        grid = [
            [0, 1, 0],
            [1, 1, 1],
            [0, 1, 0],
        ]
        # With 4-neighbors: risk = all the zeros directly adjacent
        expected_4 = [(0,0), (0,2), (2,0), (2,2)]
        result_4 = flood_risk_expand(grid, neighbors_4)
        self.assertCountEqual(result_4, expected_4,
                              msg=f"Expected {expected_4}, got {result_4} (4-neighbors)")

        # With 8-neighbors: diagonals also become risk zones (all zeros on border)
        expected_8 = [(0,0), (0,2), (2,0), (2,2)]
        # Note: here it's the same as 4-neighbors because diagonals already connect.
        result_8 = flood_risk_expand(grid, neighbors_8)
        self.assertCountEqual(result_8, expected_8,
                              msg=f"Expected {expected_8}, got {result_8} (8-neighbors)")
        
    def test_adjacent_land_detected(self):
        grid: list[list[int]] = [[0, 1]]
        expected: list[tuple[int, int]] = [(0, 0)]  # land cell next to water
        
        nei_4_return = flood_risk_expand(grid, neighbors_4)
        self.assertEqual(expected, nei_4_return,
                        msg=f"expected {expected}, returned {nei_4_return}")

        nei_8_return = flood_risk_expand(grid, neighbors_8)
        self.assertEqual(expected, nei_8_return,
                        msg=f"expected {expected}, returned {nei_8_return}")


if __name__ == "__main__":
    unittest.main()