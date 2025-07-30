import unittest

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        # Fill in your DFS or BFS logic here
        pass


class TestNumIslands(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        grid = [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
        ]
        expected = 1
        self.assertEqual(self.sol.numIslands(grid), expected)

    def test_example2(self):
        grid = [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ]
        expected = 3
        self.assertEqual(self.sol.numIslands(grid), expected)

    def test_single_land_cell(self):
        grid = [["1"]]
        expected = 1
        self.assertEqual(self.sol.numIslands(grid), expected)

    def test_single_water_cell(self):
        grid = [["0"]]
        expected = 0
        self.assertEqual(self.sol.numIslands(grid), expected)

    def test_all_land(self):
        grid = [["1","1"],["1","1"]]
        expected = 1
        self.assertEqual(self.sol.numIslands(grid), expected)

    def test_checkerboard(self):
        grid = [["1","0","1"],
                ["0","1","0"],
                ["1","0","1"]]
        expected = 5
        self.assertEqual(self.sol.numIslands(grid), expected)

if __name__ == '__main__':
    unittest.main()