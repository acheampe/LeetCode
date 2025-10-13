import unittest
from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        # TC == O(m x n), SC == (m x n)
        
        m, n = len(grid), len(grid[0])
        queue: deque[tuple[int, int, int]] = deque() # SC == (m x n) worst case scenario
        freshOranges: int = 0
        
        # multisource BFS approach
        for i in range(m): # TC == O(m x n)
            for j in range(n):
                
                if self.isRottenFruit(i, j, grid):
                    queue.append((0, i, j))
                
                if self.isFreshFruit(i, j, grid):
                    freshOranges += 1
        
        minutesForAllToRot: int = 0 # shortest path will be counted
        
        directions: list[tuple[int, int]] = [
            (0, 1), # right
            (0, -1),  # left
            (1, 0), # down
            (-1, 0) # up
        ]
        
        while queue:
            
            level, r, c = queue.popleft()
            level += 1
            
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                
                if self.isFreshFruit(nr, nc, grid):
                    grid[nr][nc] = 2 # will rot in a minute and also marks as visited
                    freshOranges -= 1
                    queue.append((level, nr, nc))
                    if level > minutesForAllToRot:
                        minutesForAllToRot += 1
                
        return minutesForAllToRot if freshOranges == 0 else -1
                
    def isFreshFruit(self, row: int, col: int, grid: list[list[int]]):
        
        if self.isWithinBound(row, col, grid): 
            return grid[row][col] == 1 # 1 == fresh fruit
        
        return False

    def isRottenFruit(self, row: int, col: int, grid: list[list[int]]):
        if self.isWithinBound(row, col, grid): 
            return grid[row][col] == 2 # 2 == fresh rotten fruit
        
        return False
    
    def isWithinBound(self, row: int, col: int, grid: list[list[int]]):
        m, n = len(grid), len(grid[0]) # will be more defensive if it was a production code
         
        if (0 <= row < m) and (0 <= col < n):
            return True
        
        return False
        
        
class TestOrangesRotting(unittest.TestCase):
    
    def setUp(self):
        self.sol = Solution()

    def test_example_0(self):
        grid = [[2,1,1],[1,1,1],[0,1,2]]
        expected = 2
        result = self.sol.orangesRotting(grid)
        self.assertEqual(result, expected, 
                         msg=f"Expected {expected} but got {result} for grid {grid}")
        
    def test_example_1(self):
        grid = [[2,1,1],[1,1,0],[0,1,1]]
        expected = 4
        result = self.sol.orangesRotting(grid)
        self.assertEqual(result, expected, 
                         msg=f"Expected {expected} but got {result} for grid {grid}")
    
    def test_example_2(self):
        grid = [[2,1,1],[0,1,1],[1,0,1]]
        expected = -1
        result = self.sol.orangesRotting(grid)
        self.assertEqual(result, expected, 
                         msg=f"Expected {expected} but got {result} for grid {grid}")
    
    def test_example_3(self):
        grid = [[0,2]]
        expected = 0
        result = self.sol.orangesRotting(grid)
        self.assertEqual(result, expected, 
                         msg=f"Expected {expected} but got {result} for grid {grid}")
    
    def test_all_rotten(self):
        grid = [[2,2,2],[2,2,2]]
        expected = 0
        result = self.sol.orangesRotting(grid)
        self.assertEqual(result, expected,
                         msg="All oranges already rotten, should return 0")
    
    def test_no_rotten(self):
        grid = [[1,1,1],[1,1,1]]
        expected = -1
        result = self.sol.orangesRotting(grid)
        self.assertEqual(result, expected,
                         msg="No rotten orange to start infection, should return -1")
    
    def test_mixed_empty(self):
        grid = [[0,1,0],[2,0,1],[0,0,0]]
        expected = -1
        result = self.sol.orangesRotting(grid)
        self.assertEqual(result, expected,
                         msg="Disconnected fresh orange should return -1")

if __name__ == "__main__":
    unittest.main()