import unittest
import copy

class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        TC and SC O(m x n)
        """
        
        m, n = len(board), len(board[0])
        directions = [(0,1), (0, -1), (1, 0), (-1,0)]
        containEdgeRegion, seen = set(), set()
        
        def validRegion(r, c, currNeighbors):
            
            if r < 0 or r >=m or c < 0 or c >= n or board[r][c] == "X" or (r, c) in containEdgeRegion or (r, c) in seen:
                return 
            
            if (not self.containEdge) and (r == 0 or r == (m - 1) or c == 0 or c == (n - 1)):
                self.containEdge = True


            currNeighbors.append((r, c))
            seen.add((r,c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                validRegion(nr, nc, currNeighbors)
                    
            
        for i in range(m):
            for j in range(n):
                
                if (i, j) not in seen and board[i][j] == "O":
                    currRegion, self.containEdge = [], False
                    validRegion(i, j, currRegion)
                    if self.containEdge:
                        for cr, cc in currRegion:
                            containEdgeRegion.add((cr, cc))

                    else:
                        for cr, cc in currRegion:
                            board[cr][cc] = "X"


class TestSurroundedRegions(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def run_case(self, board, expected):
        b = copy.deepcopy(board)
        ret = self.sol.solve(b)
        # Must modify in-place and return None
        self.assertIsNone(ret)
        self.assertEqual(b, expected)

    def test_example_1(self):
        board = [
            ["X","X","X","X"],
            ["X","O","O","X"],
            ["X","X","O","X"],
            ["X","O","X","X"]
        ]
        expected = [
            ["X","X","X","X"],
            ["X","X","X","X"],
            ["X","X","X","X"],
            ["X","O","X","X"]
        ]
        self.run_case(board, expected)

    def test_example_2_single_cell_X(self):
        board = [["X"]]
        expected = [["X"]]
        self.run_case(board, expected)

    def test_single_cell_O(self):
        board = [["O"]]
        # Border 'O' remains
        expected = [["O"]]
        self.run_case(board, expected)

    def test_all_O_small(self):
        board = [
            ["O","O"],
            ["O","O"]
        ]
        # All are border-connected -> unchanged
        expected = [
            ["O","O"],
            ["O","O"]
        ]
        self.run_case(board, expected)

    def test_center_O_captured(self):
        board = [
            ["X","X","X","X","X"],
            ["X","O","O","O","X"],
            ["X","O","X","O","X"],
            ["X","O","O","O","X"],
            ["X","X","X","X","X"]
        ]
        expected = [
            ["X","X","X","X","X"],
            ["X","X","X","X","X"],
            ["X","X","X","X","X"],
            ["X","X","X","X","X"],
            ["X","X","X","X","X"]
        ]
        self.run_case(board, expected)

    def test_border_tentacle_preserved(self):
        board = [
            ["O","X","X","X"],
            ["X","O","O","X"],
            ["X","X","O","X"],
            ["X","X","O","O"]
        ]
        # The 'O' chain on right edge connects inward—should remain 'O'
        expected = [
            ["O","X","X","X"],
            ["X","O","O","X"],
            ["X","X","O","X"],
            ["X","X","O","O"]
        ]
        self.run_case(board, expected)

    def test_no_O(self):
        board = [
            ["X","X","X"],
            ["X","X","X"],
            ["X","X","X"]
        ]
        expected = [
            ["X","X","X"],
            ["X","X","X"],
            ["X","X","X"]
        ]

    def test_snake_touching_border(self):
        board = [
            ["X","O","X","X","X"],
            ["X","O","O","O","X"],
            ["X","X","X","O","X"],
            ["X","O","O","O","X"],
            ["X","X","X","O","X"]
        ]
        # The snake reaches the top border at (0,1) -> all connected 'O's preserved
        expected = [
            ["X","O","X","X","X"],
            ["X","O","O","O","X"],
            ["X","X","X","O","X"],
            ["X","O","O","O","X"],
            ["X","X","X","O","X"]
        ]
        self.run_case(board, expected)

if __name__ == "__main__":
    unittest.main()