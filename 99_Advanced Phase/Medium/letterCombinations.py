from typing import List
import unittest
from collections import defaultdict


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        pass

                

    def mapAsciiVal(self, digits):
        """
        returns mapped asciiVals to individual phone numbers
        """
        # create map 
        digitLetterHash = defaultdict(int)
        asciiVal = ord('a')

        for i in range(2, 10): # exclusive of 10

            if i != 7 and i  != 9:
                for j in range(3):
                    if not digitLetterHash[i]:
                        digitLetterHash[i] = []
                    digitLetterHash[i].append(chr(asciiVal))
                    # increment asciiVal
                    asciiVal += 1 # for next int equivalent of chr
            
            else:
                for k in range(4):
                    # for i == 7 or i == 9
                    if not digitLetterHash[i]:
                        digitLetterHash[i] = []
                    digitLetterHash[i].append(asciiVal)
                    # increment asciiVal
                    asciiVal += 1 # for next int equivalent of chr
        
        return digitLetterHash
    
class TestLetterCombinations(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        digits = "23"
        expected_output = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        self.assertCountEqual(self.solution.letterCombinations(digits), expected_output)

    # def test_example2(self):
    #     digits = ""
    #     expected_output = []
    #     self.assertEqual(self.solution.letterCombinations(digits), expected_output)

    # def test_example3(self):
    #     digits = "2"
    #     expected_output = ["a", "b", "c"]
    #     self.assertCountEqual(self.solution.letterCombinations(digits), expected_output)

    # def test_single_digit(self):
    #     digits = "7"
    #     expected_output = ["p", "q", "r", "s"]
    #     self.assertCountEqual(self.solution.letterCombinations(digits), expected_output)

    # def test_two_digits(self):
    #     digits = "79"
    #     expected_output = [
    #         "pw", "px", "py", "pz",
    #         "qw", "qx", "qy", "qz",
    #         "rw", "rx", "ry", "rz",
    #         "sw", "sx", "sy", "sz"
    #     ]
    #     self.assertCountEqual(self.solution.letterCombinations(digits), expected_output)

    # def test_three_digits(self):
    #     digits = "234"
    #     expected_output = [
    #         "adg", "adh", "adi", "aeg", "aeh", "aei", "afg", "afh", "afi",
    #         "bdg", "bdh", "bdi", "beg", "beh", "bei", "bfg", "bfh", "bfi",
    #         "cdg", "cdh", "cdi", "ceg", "ceh", "cei", "cfg", "cfh", "cfi"
    #     ]
    #     self.assertCountEqual(self.solution.letterCombinations(digits), expected_output)

    # def test_max_digits(self):
    #     digits = "2345"  # Test with four digits
    #     expected_length = 3 * 3 * 3 * 3  # Since each digit maps to 3-4 letters, expect 3^4 combinations
    #     output = self.solution.letterCombinations(digits)
    #     self.assertEqual(len(output), expected_length)

if __name__ == "__main__":
    unittest.main()