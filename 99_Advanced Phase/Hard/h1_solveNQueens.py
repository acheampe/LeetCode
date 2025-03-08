from typing import List
import unittest

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        Return all possible distinct solutions to the N-Queens problem.

        Args:
            n (int): Size of the chessboard (n x n).

        Returns:
                List[list[str]]
        """

        # Establish space needed for operation
        allQueenPermutations = [] # O(n) space (will contain O(n!) distinct Q placements)
        board = [['.' for _ in range(n)] for _  in range(n)] # O (n^2)

        # Sets to track attacking positions
        colSet = set()
        minorDiag = set() # (r + c)
        majorDiag = set() # (r - c)

        # backtracking
        def backtracking(row):

            # Base case:
            if row == n:
                # pass (join and return)
                currPermute = [''.join(row) for row in board]
                allQueenPermutations.append(currPermute)
                return
            
            for col in range(n):
                
                # check attacking positions
                if (
                    col in colSet or 
                    (row + col) in minorDiag or
                    (row - col) in majorDiag
                ):
                    continue # skip placement

                # Add Q to board and update set
                board[row][col] = 'Q'

                colSet.add(col)
                minorDiag.add(row + col)
                majorDiag.add(row - col)

                backtracking(row + 1)

                # Backtrack to viable placements
                board[row][col] = '.'

                colSet.remove(col)
                minorDiag.remove((row + col))
                majorDiag.remove((row - col)) 

        backtracking(0)

        return allQueenPermutations



    def approachSolution(self):
        """
        Solving N queens utilizes a backtracking approach that takes advantage of 
        one queen per row and per col restriction. 

        First step: Establish and output[List[str]]. Establish n arr of n '....' in each row
        to simulate empty slot in each cell. Then establish 3 sets to track Q placement (col, posDiag, negDiag)

        from here we will establish backtracking with row as the argument (this will take care
        of one queen per row). After we will establish our base case: if row == n, we join each row into a
        list and append the list into our output arr

        After we will iterate through a column arr of n. 

        If Q is not in all three establish sets, then we place Q in (r,c) coordinates, then 
        update to all three sets accordingly. then call our bracktracking function. Before we 
        pop (r, C) and remove from all sets to backpedal from invalid paths

        By end of cycle we should have returned all possible distinct placement of queen.

        Time Complexity: O(n!), first queen has n choices, 2nd has n - 1 choices....etc
        Space Complexity: O(n * n!) --> there is n output space that stores n! of q distinct
        placement.
        """

        pass

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