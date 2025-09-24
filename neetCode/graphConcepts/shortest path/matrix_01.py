# Leetcode 542i
import unittest
class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:

        m, n = len(mat), len(mat[0]) # if this was a production code, I would be more defensive here
        trackVisited: set = set()
        
        def findMinDistance(r, c, currMinDist) -> int:
            
            if (0 > r >= m) or (0 > c >= n) or mat[r][c] == 0:
                return 0
            
            currMinDist += min(
                findMinDistance(r + 0, c + 1, currMinDist), # right
                findMinDistance(r + 0, c - 1, currMinDist), # left
                findMinDistance(r + 1, c + 0, currMinDist), # up
                findMinDistance(r - 1, c + 0, currMinDist), # down
            )
            
            mat[r][c] = currMinDist
            trackVisited.add((r, c))
            
            return 1
                
        
        for i in range(m):
            for j in range(n):
                if (i, j) not in trackVisited:
                    minDistance = float('inf')
                    findMinDistance(i, j, minDistance)
        
        return mat
        


class TestUpdateMatrix(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

#     def test_case_1(self):
#         mat = [
#             [0, 0, 0],
#             [0, 1, 0],
#             [0, 0, 0]
#         ]
#         expected = [
#             [0, 0, 0],
#             [0, 1, 0],
#             [0, 0, 0]
#         ]
#         self.assertEqual(self.sol.updateMatrix(mat), expected)

#     def test_case_2(self):
#         mat = [
#             [0, 0, 0],
#             [0, 1, 0],
#             [1, 1, 1]
#         ]
#         expected = [
#             [0, 0, 0],
#             [0, 1, 0],
#             [1, 2, 1]
#         ]
#         self.assertEqual(self.sol.updateMatrix(mat), expected)

#     def test_case_3(self):
#         mat = [
#             [1, 1, 1],
#             [1, 1, 1],
#             [0, 1, 1]
#         ]
#         expected = [
#             [2, 3, 4],
#             [1, 2, 3],
#             [0, 1, 2]
#         ]
#         self.assertEqual(self.sol.updateMatrix(mat), expected)

    def test_case_4(self):
        mat = [
            [1, 1, 0],
        ]
        expected = [
            [2, 1, 0],
        ]
        self.assertEqual(self.sol.updateMatrix(mat), expected)
        
if __name__ == '__main__':
    unittest.main()