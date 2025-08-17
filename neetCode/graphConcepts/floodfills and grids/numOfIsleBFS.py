import unittest
from collections import deque

class Solution: #TC O(m x n) SC worse case O(m x n)
    def numIslands(self, grid: list[list[str]]) -> int:
        m = len(grid)
        if m > 0:
            n = len(grid[0])
            
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque()
        count = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    queue.append((i, j))
                    grid[i][j] = '0'
                    # map out island
                    while queue:
                        
                        r, c = queue.popleft()
                
                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc
                            if ( nr >= 0 and nr < m ) and ( nc >= 0 and nc < n ) and grid[nr][nc] == '1':
                                queue.append((nr, nc))
                                grid[nr][nc] = '0'
        
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