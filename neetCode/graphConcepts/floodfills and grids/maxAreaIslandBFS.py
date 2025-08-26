import unittest
import copy
from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        
        m = len(grid)
        if m > 0:
            n = len(grid[0])
        
        else:
            return 0
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] 
        queue = deque()
        maxArea = 0 
        
        for i in range(m):
            for j in range(n):
                
                if grid[i][j] == 1:
                    currentArea = 0
                    
                    queue.append((i, j))
                    grid[i][j] = 0 
                
                    while queue:
                        
                        r, c = queue.popleft()
                        
                        currentArea += 1
                        
                        for dr, dc in directions:
                            nr, nc = dr + r, dc + c
                            if nr >= 0 and nr < m and nc >= 0 and nc < n and grid[nr][nc] == 1:
                                queue.append((nr, nc))
                                grid[nr][nc] = 0
                                
                    
                    maxArea = max(maxArea, currentArea)
        
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

    # def test_all_land_small(self):
    #     grid = [[1,1],
    #             [1,1]]
    #     expected = 4
    #     self.assertEqual(self.sol.maxAreaOfIsland(copy.deepcopy(grid)), expected)

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

    def test_large_zero_border(self):
        grid = [[0,0,0,0,0],
                [0,1,1,1,0],
                [0,1,1,1,0],
                [0,1,1,1,0],
                [0,0,0,0,0]]
        expected = 9
        self.assertEqual(self.sol.maxAreaOfIsland(copy.deepcopy(grid)), expected)

if __name__ == "__main__":
    unittest.main()