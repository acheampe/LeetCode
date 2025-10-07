# Leetcode 542
from itertools import count
from re import L
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
                
                isZero = mat[i][j]
                
                if isZero == 0 and resultMatrix[i][j] == float('inf'):
                    
                    queue.append((i, j))
                    resultMatrix[i][j] = 0.0
                
                    while queue:
                        
                        r, c = queue.popleft()
                        
                        countDistance = 0
                        for dr, dc in directions:
                            
                            nr, nc = dr + r, dc + c
                            
                            if (0 <= nr < m)  and (0 <= nc < n): # if within bound
                                
                                countDistance += 1.0
                                if mat[nr][nc] == 1:
                                    resultMatrix[nr][nc] = min(resultMatrix[nr][nc], countDistance)
                                
                                elif resultMatrix[i][j] == float('inf'):
                                    queue.append((nr, nc))
                                    resultMatrix[nr][nc] = 0.0
        
        for i in range(m):
            for j in range(n):
                
                mat[i][j] = int(resultMatrix[i][j])
                            
        return mat
                    
                    
        
        
    


        



class TestUpdateMatrix(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    # def test_case_4(self):
    #     mat = [
    #         [1, 1, 0],
    #     ]
    #     expected = [
    #         [2, 1, 0],
    #     ]
    #     self.assertEqual(self.sol.updateMatrix(mat), expected)
        
    def test_case_0(self):
        mat = [
            [1, 0],
        ]
        expected = [
            [1, 0],
        ]
        self.assertEqual(self.sol.updateMatrix(mat), expected)

    # def test_case_1(self):
    #     mat = [
    #         [0, 0, 0],
    #         [0, 1, 0], 
    #         [0, 0, 0] 
    #     ]
    #     expected = [
    #         [0, 0, 0],
    #         [0, 1, 0],
    #         [0, 0, 0]
    #     ]
    #     self.assertEqual(self.sol.updateMatrix(mat), expected)

    # def test_case_2(self):
    #     mat = [
    #         [0, 0, 0],
    #         [0, 1, 0],
    #         [1, 1, 1]
    #     ]
    #     expected = [
    #         [0, 0, 0],
    #         [0, 1, 0],
    #         [1, 2, 1]
    #     ]
    #     self.assertEqual(self.sol.updateMatrix(mat), expected)

    # def test_case_3(self):
    #     mat = [
    #         [1, 1, 1],
    #         [1, 1, 1],
    #         [0, 1, 1]
    #     ]
    #     expected = [
    #         [2, 3, 4],
    #         [1, 2, 3],
    #         [0, 1, 2]
    #     ]
    #     self.assertEqual(self.sol.updateMatrix(mat), expected)
    
    # def test_case_5(self):
    #     mat = [
    #         [1, 1, 0],
    #         [1, 1, 1]
    #     ]
    #     expected = [
    #         [2, 1, 0],
    #         [3, 2, 1]
    #     ]
    #     self.assertEqual(self.sol.updateMatrix(mat), expected)
        
    # def test_case_6(self):
    #     mat = [[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],[0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,1,1,1,0,1],[1,1,1,1,1,1,1,0,1,0],[1,1,1,1,0,1,0,0,1,1]]
    #     expected = [[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],[0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,2,1,1,0,1],[2,1,1,1,1,2,1,0,1,0],[3,2,2,1,0,1,0,0,1,1]]
    #     self.assertEqual(self.sol.updateMatrix(mat), expected)
        
if __name__ == '__main__':
    unittest.main()