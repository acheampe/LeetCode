from typing import List
import unittest

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        Return all possible distinct solutions to the N-Queens problem.

        Args:
            n (int): Size of the chessboard (n x n).

        Returns:
            List[List[str]]: A list of valid chessboard configurations.

        Space Complexity: O(n!)
        Time Complexity: O(n + n!) worst case scenario
        """

        allPossibleComb = []  # output of our final solution
        chessPlacement = [['.'] * n for _ in range(n)]  # Initialize empty board

        # Sets to track column and diagonal conflicts
        usedColumns = set()
        minorDiagonal = set()  # row + col
        majorDiagonal = set()  # row - col

        def backtracking(row):
            """Recursive function to place queens row by row."""
            # Base Case: All queens placed
            if row == n:
                allPossibleComb.append(["".join(row) for row in chessPlacement])
                return

            for col in range(n):
                # Check if placing a queen at (row, col) is safe
                if col in usedColumns or (row + col) in minorDiagonal or (row - col) in majorDiagonal:
                    continue  # Skip this placement

                # Place the queen
                chessPlacement[row][col] = 'Q'
                usedColumns.add(col)
                minorDiagonal.add(row + col)
                majorDiagonal.add(row - col)

                # Recur to place next queen
                backtracking(row + 1)

                # Backtrack: Remove the queen
                chessPlacement[row][col] = '.'
                usedColumns.remove(col)
                minorDiagonal.remove(row + col)
                majorDiagonal.remove(row - col)

        # Start backtracking from row 0
        backtracking(0)

        return allPossibleComb

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

    # def test_example2(self):
    #     n = 1
    #     expected_output = [["Q"]]
    #     result = self.solution.solveNQueens(n)
    #     self.assertEqual(result, expected_output)

    # def test_no_duplicate_solutions(self):
    #     n = 5
    #     result = self.solution.solveNQueens(n)
    #     self.assertEqual(len(result), len(set(tuple(board) for board in result)))

    # def test_valid_board_structure(self):
    #     n = 6
    #     result = self.solution.solveNQueens(n)
    #     for board in result:
    #         self.assertEqual(len(board), n)  # Ensure n rows
    #         for row in board:
    #             self.assertEqual(len(row), n)  # Ensure n columns
    #             self.assertEqual(row.count("Q"), 1)  # Each row should have exactly 1 queen

    # def test_no_queen_attacks(self):
    #     """ Ensure that no two queens attack each other """
    #     n = 7
    #     result = self.solution.solveNQueens(n)
    #     for board in result:
    #         queen_positions = []
    #         for r in range(n):
    #             for c in range(n):
    #                 if board[r][c] == "Q":
    #                     queen_positions.append((r, c))
            
    #         # Check if queens attack each other
    #         for i, (r1, c1) in enumerate(queen_positions):
    #             for j, (r2, c2) in enumerate(queen_positions):
    #                 if i != j:
    #                     self.assertNotEqual(r1, r2)  # Same row
    #                     self.assertNotEqual(c1, c2)  # Same column
    #                     self.assertNotEqual(abs(r1 - r2), abs(c1 - c2))  # Diagonal attack

if __name__ == "__main__":
    unittest.main()