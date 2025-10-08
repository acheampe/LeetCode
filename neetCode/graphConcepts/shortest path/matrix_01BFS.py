# Leetcode 542
import unittest
from collections import deque
class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        
        m, n = len(mat), len(mat[0])
        queue: deque[tuple[int, int]] = deque()
        directions: list[tuple[int, int]] = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        resultMatrix: list[list[float]] = [[float('inf') for _ in range(n)] for _ in range(m)]
        
        
        for i in range(m):
            for j in range(n):
               
               if mat[i][j] == 0:
                   resultMatrix[i][j] = 0
                   queue.append((i, j))
                   
        while queue:
            
            r, c = queue.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if (0 <= nr < m) and (0 <= nc < n) and resultMatrix[nr][nc] > \
                resultMatrix[r][c] + 1:
                    resultMatrix[nr][nc] = resultMatrix[r][c] + 1
                    queue.append((nr, nc))
                            
        return resultMatrix
                    
                    
        
        
    


        



class TestUpdateMatrix(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_case_5(self):
        mat = [
            [1, 1, 0],
            [1, 1, 1]
        ]
        expected = [
            [2, 1, 0],
            [3, 2, 1]
        ]
        self.assertEqual(self.sol.updateMatrix(mat), expected)
    
    def test_case_4(self):
        mat = [
            [1, 1, 0],
        ]
        expected = [
            [2, 1, 0],
        ]
        self.assertEqual(self.sol.updateMatrix(mat), expected)
        
    def test_case_0(self):
        mat = [
            [1, 0],
        ]
        expected = [
            [1, 0],
        ]
        self.assertEqual(self.sol.updateMatrix(mat), expected)

    def test_case_1(self):
        mat = [
            [0, 0, 0],
            [0, 1, 0], 
            [0, 0, 0] 
        ]
        expected = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
        self.assertEqual(self.sol.updateMatrix(mat), expected)

    def test_case_2(self):
        mat = [
            [0, 0, 0],
            [0, 1, 0],
            [1, 1, 1]
        ]
        expected = [
            [0, 0, 0],
            [0, 1, 0],
            [1, 2, 1]
        ]
        self.assertEqual(self.sol.updateMatrix(mat), expected)

    def test_case_3(self):
        mat = [
            [1, 1, 1],
            [1, 1, 1],
            [0, 1, 1]
        ]
        expected = [
            [2, 3, 4],
            [1, 2, 3],
            [0, 1, 2]
        ]
        self.assertEqual(self.sol.updateMatrix(mat), expected)
        
    def test_case_6(self):
        mat = [[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],[0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,1,1,1,0,1],[1,1,1,1,1,1,1,0,1,0],[1,1,1,1,0,1,0,0,1,1]]
        expected = [[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],[0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,2,1,1,0,1],[2,1,1,1,1,2,1,0,1,0],[3,2,2,1,0,1,0,0,1,1]]
        self.assertEqual(self.sol.updateMatrix(mat), expected)
        
if __name__ == '__main__':
    unittest.main()