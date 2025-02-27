from typing import List
import unittest

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        returns all permutations of digits mapped to letters

        Args: string

        Return: List[str]

        Time Complexity (exponential) = O(4^n), worst case scenario, a digit can map up to 4 digits
        Space Complexity = O(n), we recurse ones per digit so recursion depth is O(n)
        """

        # Establish variables needed
        # Hard coding to improve efficiency, comes at a cost of flexibility
        mappedDigits = {
            '2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], 
            '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], 
            '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], 
            '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']
                        }
        
        self.allCombinations = [] # arr of str

        def findAllComb(digitArr, index, currComb):
            """
            returns the current combination of digits
            """

            # Base/termination case
            if len(digitArr) == len(currComb):
                self.allCombinations.append(''.join(currComb))
                return
            
            # Combine letters through tree recursion
            for letter in mappedDigits[digitArr[index]]:
                currComb.append(letter)

                findAllComb(digitArr, index + 1, currComb)

                # backtrack
                currComb.pop()

        if digits: # make sure digit is not empty
            findAllComb([digit for digit in digits], 0, [])
          
        return self.allCombinations


    
def approachSolution(self):
    """
    The approach to solving this problem relies on applying backtracking effectively.

    **Step 1: Hardcode the digit-to-letter mapping using a dictionary.**
      - This ensures efficient retrieval.
      - Trade-off: Less modular but optimal for this specific problem.

    **Step 2: Define a recursive backtracking function** with arguments:
      - `digits` (input as an array),
      - `index` (to track recursion depth),
      - `currComb` (the current combination being formed).

    **Step 3: Establish the base case for recursion.**
      - If `index == len(digits)`, we have a complete combination.
      - Append `currComb` (joined into a string) to our result array.

    **Step 4: Loop through possible letters for the current digit.**
      - Add each letter to `currComb`, then recursively call the function
        while incrementing `index` to move to the next digit.
      - After recursion, backtrack by popping the last letter.

    **Step 5: The backtracking process ensures we explore all valid combinations.**
      - Once all recursive calls finish, we have generated all letter combinations.

    **Time Complexity: O(4^n)**
      - This is a combination problem where each digit contributes up to 4 choices.
      - The total number of recursive calls follows the branching factor of `4^n`.

    **Space Complexity: O(n)**
      - The recursive stack depth grows to at most `n` (the number of digits).
      - There is no additional auxiliary data structure beyond the recursion stack.
    """

    pass
    
class TestLetterCombinations(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        digits = "23"
        expected_output = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        self.assertCountEqual(self.solution.letterCombinations(digits), expected_output)

    def test_example2(self):
        digits = ""
        expected_output = []
        self.assertEqual(self.solution.letterCombinations(digits), expected_output)

    def test_example3(self):
        digits = "2"
        expected_output = ["a", "b", "c"]
        self.assertCountEqual(self.solution.letterCombinations(digits), expected_output)

    def test_single_digit(self):
        digits = "7"
        expected_output = ["p", "q", "r", "s"]
        self.assertCountEqual(self.solution.letterCombinations(digits), expected_output)

    def test_two_digits(self):
        digits = "79"
        expected_output = [
            "pw", "px", "py", "pz",
            "qw", "qx", "qy", "qz",
            "rw", "rx", "ry", "rz",
            "sw", "sx", "sy", "sz"
        ]
        self.assertCountEqual(self.solution.letterCombinations(digits), expected_output)

    def test_three_digits(self):
        digits = "234"
        expected_output = [
            "adg", "adh", "adi", "aeg", "aeh", "aei", "afg", "afh", "afi",
            "bdg", "bdh", "bdi", "beg", "beh", "bei", "bfg", "bfh", "bfi",
            "cdg", "cdh", "cdi", "ceg", "ceh", "cei", "cfg", "cfh", "cfi"
        ]
        self.assertCountEqual(self.solution.letterCombinations(digits), expected_output)

    def test_max_digits(self):
        digits = "2345"  # Test with four digits
        expected_length = 3 * 3 * 3 * 3  # Since each digit maps to 3-4 letters, expect 3^4 combinations
        output = self.solution.letterCombinations(digits)
        self.assertEqual(len(output), expected_length)

if __name__ == "__main__":
    unittest.main()