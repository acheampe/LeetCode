import unittest
from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        pass  # Implementation goes here

class TestSolveNQueens(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        n = 4
        expected_output = [
            [".Q..", "...Q", "Q...", "..Q."],
            ["..Q.", "Q...", "...Q", ".Q.."]
        ]
        result = self.solution.solveNQueens(n)
        self.assertCountEqual(result, expected_output)

    def test_example2(self):
        n = 1
        expected_output = [["Q"]]
        result = self.solution.solveNQueens(n)
        self.assertEqual(result, expected_output)

    def test_no_duplicate_solutions(self):
        n = 5
        result = self.solution.solveNQueens(n)
        self.assertEqual(len(result), len(set(tuple(board) for board in result)))

    def test_valid_board_structure(self):
        n = 6
        result = self.solution.solveNQueens(n)
        for board in result:
            self.assertEqual(len(board), n)  # Ensure n rows
            for row in board:
                self.assertEqual(len(row), n)  # Ensure n columns
                self.assertEqual(row.count("Q"), 1)  # Each row should have exactly 1 queen

    def test_no_queen_attacks(self):
        """ Ensure that no two queens attack each other """
        n = 7
        result = self.solution.solveNQueens(n)
        for board in result:
            queen_positions = []
            for r in range(n):
                for c in range(n):
                    if board[r][c] == "Q":
                        queen_positions.append((r, c))
            
            # Check if queens attack each other
            for i, (r1, c1) in enumerate(queen_positions):
                for j, (r2, c2) in enumerate(queen_positions):
                    if i != j:
                        self.assertNotEqual(r1, r2)  # Same row
                        self.assertNotEqual(c1, c2)  # Same column
                        self.assertNotEqual(abs(r1 - r2), abs(c1 - c2))  # Diagonal attack

if __name__ == "__main__":
    unittest.main()