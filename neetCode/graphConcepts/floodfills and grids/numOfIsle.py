import unittest

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:

        m, n = len(grid), len(grid[0])
        count = 0
        mapped = set() # meaning we have marked this as part of an island
        directions = [[0, 1], [0,  -1], [1, 0], [-1, 0]]
        
        def mapIsland(r , c):
            
            # create base case
            if (r, c) in mapped or ( r < 0 or r >= m ) or ( c < 0 or c >= n) or grid[r][c] == "0":
                return 
            
            # add to mapped Island
            mapped.add((r, c))
            
            for dr, dc in directions:
                mapIsland(dr + r, dc + c)
        
        for i in range(m):
            for j in range(n):
                
                if (i, j) not in mapped and grid[i][j] == "1":
                    # count it as an island
                    count += 1
                    mapIsland(i, j)
        
        return count

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