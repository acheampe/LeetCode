import unittest

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        # Fill in your DFS or BFS logic here
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # up, down, left, right
        m, n = len(grid), len(grid[0])
        seen = set()
        count = 0 
        
        def isIsland(x, y):
            
            # base cases
            if (0 > x  or x => m) or (0 > y or y => n) or grid[x][y] == 0:
                return True # out of bounds are assumed to be zeros, and all coords need to be 0 to quantify surroundings as an Island
            
            if (x, y) in seen or grid[x][y] == 1:
                return False # already marked

  
            if isIsland(-1 + x, 0 + y) and isIsland(1 + x, 0 + y)  and isIsland(0 + x, 1 + y) and isIsland(0 + x, -1 + y):
                count += 1
            
        
        for i in range(m):
            for j in range(n):
                isIsland(i, j)
        return count
        


class TestNumIslands(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    # def test_example1(self):
    #     grid = [
    #         ["1","1","1","1","0"],
    #         ["1","1","0","1","0"],
    #         ["1","1","0","0","0"],
    #         ["0","0","0","0","0"]
    #     ]
    #     expected = 1
    #     self.assertEqual(self.sol.numIslands(grid), expected)

    # def test_example2(self):
    #     grid = [
    #         ["1","1","0","0","0"],
    #         ["1","1","0","0","0"],
    #         ["0","0","1","0","0"],
    #         ["0","0","0","1","1"]
    #     ]
    #     expected = 3
    #     self.assertEqual(self.sol.numIslands(grid), expected)

    # def test_single_land_cell(self):
    #     grid = [["1"]]
    #     expected = 1
    #     self.assertEqual(self.sol.numIslands(grid), expected)

    # def test_single_water_cell(self):
    #     grid = [["0"]]
    #     expected = 0
    #     self.assertEqual(self.sol.numIslands(grid), expected)

    # def test_all_land(self):
    #     grid = [["1","1"],["1","1"]]
    #     expected = 1
    #     self.assertEqual(self.sol.numIslands(grid), expected)

    def test_checkerboard(self):
        grid = [["1","0","1"],
                ["0","1","0"],
                ["1","0","1"]]
        expected = 5
        self.assertEqual(self.sol.numIslands(grid), expected)

if __name__ == '__main__':
    unittest.main()