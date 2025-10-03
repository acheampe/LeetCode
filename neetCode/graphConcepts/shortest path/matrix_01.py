# Leetcode 542
import unittest


class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:

        m, n = len(mat), len(mat[0]) # if this was a production code, I would be more defensive here
        
        memo: dict[tuple[int, int], float] = {}
        curr_path: set[tuple[int, int]] = set()
        
        def findMinDistance(r, c) -> float:
            
            # if OOB
            if (0 > r or r >= m) or (0 > c or c >= n) or (r, c) in curr_path:
                return float('inf')
            
            # if cell is zero
            if mat[r][c] == 0:
                return 0
            
            # utilize memo to reduce recursive dependence
            if (r, c) in memo:
                return memo[(r, c)]
            
            curr_path.add((r, c))
            result = [
                findMinDistance(r, c + 1),
                            findMinDistance(r, c - 1),
                            findMinDistance(r - 1, c),
                            findMinDistance(r + 1, c,)
            ]
            
            curr_path.remove((r, c))
            
            min_dist =  min(result)
            
            if min_dist == float('inf'):
                return float('inf')

            dist = min_dist + 1.0
            memo[(r, c)] = dist
            
            return dist
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] != 0:
                    findMinDistance(i, j)

        for i in range(m):
            for j in range(n):
                if mat[i][j] != 0:
                    mat[i][j] = int(memo[(i, j)])
        
        return mat


class TestUpdateMatrix(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

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

    def test_case_4(self):
        mat = [
            [1, 1, 0],
        ]
        expected = [
            [2, 1, 0],
        ]
        self.assertEqual(self.sol.updateMatrix(mat), expected)
    
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
        
    # def test_case_6(self):
    #     mat = [[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],[0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,1,1,1,0,1],[1,1,1,1,1,1,1,0,1,0],[1,1,1,1,0,1,0,0,1,1]]
    #     expected = [[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],[0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,2,1,1,0,1],[2,1,1,1,1,2,1,0,1,0],[3,2,2,1,0,1,0,0,1,1]]
    #     self.assertEqual(self.sol.updateMatrix(mat), expected)
        
if __name__ == '__main__':
    unittest.main()