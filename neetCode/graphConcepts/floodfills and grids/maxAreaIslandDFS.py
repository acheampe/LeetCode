import unittest
import copy

class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        m = len(grid)
        if m:
            n = len(grid[0])
        
        else: 
            return 0 # for an early return
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        maxArea = 0
        
        def calcAreaDFS(r, c):
            
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != 1:
                return 0
            

            grid[r][c] = 0
            total = 1
            for dr, dc in directions:
                total += calcAreaDFS(r + dr, c + dc)
                    
        
            return total # LIFO principle (return 1) and add to current total
        
        for i in range(m):
            for j in range(n):
                
                if grid[i][j] == 1:
                    maxArea = max(calcAreaDFS(i, j), maxArea)
                    
        return maxArea

class TestMaxAreaOfIsland(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    # def test_example_1(self):
    #     grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
    #             [0,0,0,0,0,0,0,1,1,1,0,0,0],
    #             [0,1,1,0,1,0,0,0,0,0,0,0,0],
    #             [0,1,0,0,1,1,0,0,1,0,1,0,0],
    #             [0,1,0,0,1,1,0,0,1,1,1,0,0],
    #             [0,0,0,0,0,0,0,0,0,0,1,0,0],
    #             [0,0,0,0,0,0,0,1,1,1,0,0,0],
    #             [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    #     expected = 6
    #     self.assertEqual(self.sol.maxAreaOfIsland(copy.deepcopy(grid)), expected)

    # def test_example_2(self):
    #     grid = [[0,0,0,0,0,0,0,0]]
    #     expected = 0
    #     self.assertEqual(self.sol.maxAreaOfIsland(copy.deepcopy(grid)), expected)

    # def test_single_cell_land(self):
    #     grid = [[1]]
    #     expected = 1
    #     self.assertEqual(self.sol.maxAreaOfIsland(copy.deepcopy(grid)), expected)

    # def test_single_cell_water(self):
    #     grid = [[0]]
    #     expected = 0
    #     self.assertEqual(self.sol.maxAreaOfIsland(copy.deepcopy(grid)), expected)

    def test_all_land_small(self):
        grid = [[1,1],
                [1,1]]
        expected = 4
        self.assertEqual(self.sol.maxAreaOfIsland(copy.deepcopy(grid)), expected)

    # def test_multiple_disjoint_islands(self):
    #     grid = [[1,0,1,0],
    #             [0,0,0,0],
    #             [1,0,1,1]]
    #     # islands: sizes 1,1,1,2 -> max = 2
    #     expected = 2
    #     self.assertEqual(self.sol.maxAreaOfIsland(copy.deepcopy(grid)), expected)

    # def test_snake_shape(self):
    #     grid = [[1,1,1,1,1]]
    #     expected = 5
    #     self.assertEqual(self.sol.maxAreaOfIsland(copy.deepcopy(grid)), expected)

    # def test_vertical_bar(self):
    #     grid = [[1],[1],[1],[0],[1]]
    #     expected = 3
    #     self.assertEqual(self.sol.maxAreaOfIsland(copy.deepcopy(grid)), expected)

    # def test_checkerboard(self):
    #     grid = [[1,0,1,0],
    #             [0,1,0,1],
    #             [1,0,1,0],
    #             [0,1,0,1]]
    #     # no 4-directional adjacency; max island area = 1
    #     expected = 1
    #     self.assertEqual(self.sol.maxAreaOfIsland(copy.deepcopy(grid)), expected)

    # def test_large_zero_border(self):
    #     grid = [[0,0,0,0,0],
    #             [0,1,1,1,0],
    #             [0,1,1,1,0],
    #             [0,1,1,1,0],
    #             [0,0,0,0,0]]
    #     expected = 9
    #     self.assertEqual(self.sol.maxAreaOfIsland(copy.deepcopy(grid)), expected)

if __name__ == "__main__":
    unittest.main()