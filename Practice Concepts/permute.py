import unittest
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        return all permutations of input array
        """

        self.result = []
        
        self.backtracking(nums, [])

        return self.result
    
    def backtracking(self, nums, currPermute):
        """
        backtrack to select permutations
        """
        # Termination / return condition
        if len(nums) == len(currPermute):
            self.result.append(currPermute[:])
            return 

        for i in range(len(nums)):

            if nums[i] in currPermute:
                continue # To avoid duplicates O(n)

            currPermute.append(nums[i])

            self.backtracking(nums, currPermute)

            # backtrack
            currPermute.pop()

class TestPermute(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        nums = [1, 2, 3]
        expected_output = [
            [1, 2, 3], [1, 3, 2],
            [2, 1, 3], [2, 3, 1],
            [3, 1, 2], [3, 2, 1]
        ]
        self.assertCountEqual(self.solution.permute(nums), expected_output)

    def test_example2(self):
        nums = [0, 1]
        expected_output = [
            [0, 1], [1, 0]
        ]
        self.assertCountEqual(self.solution.permute(nums), expected_output)

    def test_example3(self):
        nums = [1]
        expected_output = [
            [1]
        ]
        self.assertCountEqual(self.solution.permute(nums), expected_output)

    def test_empty_input(self):
        nums = []
        expected_output = [[]]
        self.assertCountEqual(self.solution.permute(nums), expected_output)

    def test_large_input(self):
        nums = [1, 2, 3, 4]
        # Expected output contains all permutations of nums
        expected_output = [
            [1, 2, 3, 4], [1, 2, 4, 3], [1, 3, 2, 4], [1, 3, 4, 2], [1, 4, 2, 3], [1, 4, 3, 2],
            [2, 1, 3, 4], [2, 1, 4, 3], [2, 3, 1, 4], [2, 3, 4, 1], [2, 4, 1, 3], [2, 4, 3, 1],
            [3, 1, 2, 4], [3, 1, 4, 2], [3, 2, 1, 4], [3, 2, 4, 1], [3, 4, 1, 2], [3, 4, 2, 1],
            [4, 1, 2, 3], [4, 1, 3, 2], [4, 2, 1, 3], [4, 2, 3, 1], [4, 3, 1, 2], [4, 3, 2, 1]
        ]
        self.assertCountEqual(self.solution.permute(nums), expected_output)

    def test_negative_numbers(self):
        nums = [-1, -2, -3]
        expected_output = [
            [-1, -2, -3], [-1, -3, -2],
            [-2, -1, -3], [-2, -3, -1],
            [-3, -1, -2], [-3, -2, -1]
        ]
        self.assertCountEqual(self.solution.permute(nums), expected_output)

    def test_mixed_numbers(self):
        nums = [-1, 0, 1]
        expected_output = [
            [-1, 0, 1], [-1, 1, 0],
            [0, -1, 1], [0, 1, -1],
            [1, -1, 0], [1, 0, -1]
        ]
        self.assertCountEqual(self.solution.permute(nums), expected_output)

if __name__ == "__main__":
    unittest.main()