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
        rowLength = len(board)
        colLength = len(board[0])

        def backtracking(r, c, index, currPath):
            """explores all paths to try to find valid path"""
            
            # Base case: True
            if len(word) == index:
                return True
            
            # Base Cases: False
            # Boundary validation check
            if not (0 <= r < rowLength) or not (0 <= c < colLength):
                return False
            # Valid path check
            if board[r][c] != word[index] or (r, c) in currPath:
                return False
            
            # after base conditions are not met we add coordinates to valid path
            currPath.add((r, c))

            isNextPath = (
                # explore all paths O(4^n)
                backtracking(r + 1, c, index + 1, currPath) or                
                backtracking(r - 1, c, index + 1, currPath) or              
                backtracking(r, c + 1, index + 1, currPath) or             
                backtracking(r, c - 1, index + 1, currPath)  
            )

            # backtrack
            currPath.remove((r, c))

            return isNextPath

        for row in range(rowLength):
            for col in range(colLength):

                if backtracking(row, col, 0, set()):
                    return True
        
        return False # after exhausting all paths 

    def approachSolution(self):
        """
        The approach to this problem requires exploration of all possible letters
        and adjacent direction. Therefore the best approach will be through a bruteforce
        solution to exhaust all paths. 

        The first step to approach this is to declare length of row and length of 
        column derived from board matrix. Followed by declaring a set to track
        viable visited paths

        from here we establish a backtracking algo to return a viable path with 
        cell coordinates as arguments and current index of word search. Just like
        any backtracking solution we must establish base case. In this particular 
        case true and false return base cases.

        A true base case returns true when index arg == len(word) and a false base case
        occurs under exceed boundary conditions, or if current cell is already in visited and if
        current letter in word does not match letter in cell.

        if bases cases are not met, then we add current cell coordinates to valid path
        the recall backtracking algo to explore all 4 directions for the next valid path and if no valid
        path is scene we back track by removing the latest coordinates from set

        From here we write a funct to iterate through board that initiate the backtracking
        algo.

        if a path is found we return true, if it isn't then we return false

        Time Complexity: O(n * m * 4^n)
        Space Complexity: O(n)
        """

        pass

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