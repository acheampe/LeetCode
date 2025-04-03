import unittest

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = {}  # keys are (i//3, j//3)
        
        # overall SC O(n) and TC O(n^2)
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue

                if val in rows[i] or val in cols[j] or val in boxes.get((i//3, j//3), set()):
                    return False

                rows[i].add(val)
                cols[j].add(val)
                boxes.setdefault((i//3, j//3), set()).add(val)

        return True
        

class TestValidSudoku(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1_valid(self):
        board = [
            ["1","2",".",".","3",".",".",".","."],
            ["4",".",".","5",".",".",".",".","."],
            [".","9","8",".",".",".",".",".","3"],
            ["5",".",".",".","6",".",".",".","4"],
            [".",".",".","8",".","3",".",".","5"],
            ["7",".",".",".","2",".",".",".","6"],
            [".",".",".",".",".",".","2",".","."],
            [".",".",".","4","1","9",".",".","8"],
            [".",".",".",".","8",".",".","7","9"]
        ]
        self.assertTrue(self.sol.isValidSudoku(board))

    # def test_example_2_invalid_sub_box(self):
    #     board = [
    #         ["1","2",".",".","3",".",".",".","."],
    #         ["4",".",".","5",".",".",".",".","."],
    #         [".","9","1",".",".",".",".",".","3"],
    #         ["5",".",".",".","6",".",".",".","4"],
    #         [".",".",".","8",".","3",".",".","5"],
    #         ["7",".",".",".","2",".",".",".","6"],
    #         [".",".",".",".",".",".","2",".","."],
    #         [".",".",".","4","1","9",".",".","8"],
    #         [".",".",".",".","8",".",".","7","9"]
    #     ]
    #     self.assertFalse(self.sol.isValidSudoku(board))

    # def test_invalid_row(self):
    #     board = [
    #         ["5","3",".",".","7",".",".",".","."],
    #         ["6",".",".","1","9","5",".",".","."],
    #         [".","9","8",".",".",".",".","6","."],
    #         ["8",".",".",".","6",".",".",".","3"],
    #         ["4",".",".","8",".","3",".",".","1"],
    #         ["7",".",".",".","2",".",".",".","6"],
    #         [".","6",".",".",".",".","2","8","."],
    #         [".",".",".","4","1","9",".",".","5"],
    #         [".",".",".",".","8",".",".","7","5"]  # duplicate 5 in row
    #     ]
    #     self.assertFalse(self.sol.isValidSudoku(board))

    # def test_invalid_column(self):
    #     board = [
    #         ["8","3",".",".","7",".",".",".","."],
    #         ["6",".",".","1","9","5",".",".","."],
    #         [".","9","8",".",".",".",".","6","."],
    #         ["8",".",".",".","6",".",".",".","3"],  # duplicate 8 in column
    #         ["4",".",".","8",".","3",".",".","1"],
    #         ["7",".",".",".","2",".",".",".","6"],
    #         [".","6",".",".",".",".","2","8","."],
    #         [".",".",".","4","1","9",".",".","5"],
    #         [".",".",".",".","8",".",".","7","9"]
    #     ]
    #     self.assertFalse(self.sol.isValidSudoku(board))

    # def test_empty_board(self):
    #     board = [["."]*9 for _ in range(9)]
    #     self.assertTrue(self.sol.isValidSudoku(board))

if __name__ == '__main__':
    unittest.main()