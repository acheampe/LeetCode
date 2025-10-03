# Leetcode 542
import unittest


class Solution:
    # Not that a DFS does not gaurantee shortest path
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        
        # first cacl the len of rows and len
        m, n = len(mat), len(mat[0])
        
        # initialize current_path DS (set) and memoization (dic)
        memo: dict[tuple[int, int], float] = dict()
        curr_path: set[tuple[int, int]] = set()
        
        # set up recur func with coordination as an argument
        def dfs(r, c):
        
            # first condition: if OOB or in curr_path return 'inf'
            if (0 > r or r >= m) or (0 > c or c >= n) or (r, c) in curr_path:
                return float('inf')
            
            # second condition: if coord points to cell with zero, return zero
            if mat[r][c] == 0:
                return 0
            
            # third condition: if coord in memo: return value from memo
            if (r, c) in memo:
                return memo[(r, c)]
            
            ### Otherwise lets set up recursion
            
            # add coord to current path
            curr_path.add((r, c))
            # then calc distance:
              # dist = [4 recur calls in each direction]
            
            distance = [
                dfs(r, c + 1),
                dfs(r, c - 1),
                dfs(r + 1, c),
                dfs(r - 1, c),
                ]
            
            curr_path.remove((r, c))
            min_dist = min(distance)
            
            # calc min distance:
            if min_dist == float('inf'): # it shouldnt under given conditions for problem
                return min_dist
            
            memo[(r, c)] = min_dist + 1
            
            return min_dist + 1
            
        
        # iter through mat
        # if coord points to a cell with zero, then skip, else initiate dfs
        for i in range(m):
            for j in range(n):
                
                if mat[i][j] != 0:
                    dfs(i, j)
        
        # iterate through mat and if coord is not zero - reference memo to update mat accordingly
        for i in range(m):
            for j in range(n):
                
                if mat[i][j] != 0:
                    mat[i][j] = int(memo[(i, j)])
                    
        # return mat
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