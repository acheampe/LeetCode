import unittest
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Return true if the word is present in the matrix.

        Args:
            board (List[List[str]]): 2D character grid
            word (str): Target word to search

        Returns:
            bool: True if word exists, False otherwise

        Time Complexity: O(m * n * 4^n) (explores up to 4 paths per character)
        Space Complexity: O(n) (recursive depth of word length)
        """
        rowLength, colLength = len(board), len(board[0])

        # Recursive DFS backtracking
        def backtracking(rowIndex, colIndex, wordIndex, visitedCoordinates):
            # Base case: word found
            if wordIndex == len(word):
                return True
            
            # Boundary and invalid conditions
            if not (0 <= rowIndex < rowLength and 0 <= colIndex < colLength):
                return False
            if (rowIndex, colIndex) in visitedCoordinates or board[rowIndex][colIndex] != word[wordIndex]:
                return False
            
            # Mark as visited
            visitedCoordinates.add((rowIndex, colIndex))

            # Explore all four directions
            found = (
                backtracking(rowIndex + 1, colIndex, wordIndex + 1, visitedCoordinates) or
                backtracking(rowIndex - 1, colIndex, wordIndex + 1, visitedCoordinates) or
                backtracking(rowIndex, colIndex + 1, wordIndex + 1, visitedCoordinates) or
                backtracking(rowIndex, colIndex - 1, wordIndex + 1, visitedCoordinates)
            )

            # Backtrack (undo visit)
            visitedCoordinates.remove((rowIndex, colIndex))
            return found
        
        # Try to start from every cell in the board
        for i in range(rowLength):
            for j in range(colLength):
                if backtracking(i, j, 0, set()):  # Pass a new set for each path
                    return True
        
        return False  # No valid path found


class TestWordSearch(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        board = [["A","B","C","E"],
                 ["S","F","C","S"],
                 ["A","D","E","E"]]
        word = "ABCCED"
        self.assertTrue(self.solution.exist(board, word))

    def test_example2(self):
        board = [["A","B","C","E"],
                 ["S","F","C","S"],
                 ["A","D","E","E"]]
        word = "SEE"
        self.assertTrue(self.solution.exist(board, word))

    def test_example3(self):
        board = [["A","B","C","E"],
                 ["S","F","C","S"],
                 ["A","D","E","E"]]
        word = "ABCB"
        self.assertFalse(self.solution.exist(board, word))

    def test_single_letter_board(self):
        board = [["A"]]
        word = "A"
        self.assertTrue(self.solution.exist(board, word))

    def test_single_letter_not_found(self):
        board = [["A"]]
        word = "B"
        self.assertFalse(self.solution.exist(board, word))

    def test_word_longer_than_board(self):
        board = [["A","B","C"], ["D","E","F"]]
        word = "ABCDEFG"
        self.assertFalse(self.solution.exist(board, word))

    def test_vertical_and_horizontal_movement(self):
        board = [["A","B"], ["C","D"]]
        word = "ACD"
        self.assertTrue(self.solution.exist(board, word)) 

    def test_full_board_traversal(self):
        board = [["A","B","C"],
                 ["D","E","F"],
                 ["G","H","I"]]
        word = "ABCDEFGHI"
        self.assertFalse(self.solution.exist(board, word))

    def test_reuse_of_same_cell(self):
        board = [["A","B","C"],
                 ["D","E","F"],
                 ["G","H","I"]]
        word = "ABA"
        self.assertFalse(self.solution.exist(board, word))

if __name__ == "__main__":
    unittest.main()