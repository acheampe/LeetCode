import unittest
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        return all permutations on nums
        Time Complexity = O(n * n!) / can be O(n!) if a set is used instead of a list
        Space Complexity = O(h)
        """
        result = []

        self.backTrack(nums, [], result)
        
        return result

            
    
    def backTrack(self, arr, currPermute, result):
        """
        return permutation of given num
        """

        # Terminantion condition:
        if len(currPermute) == len(arr):
            result.append(currPermute[:]) #  each permutation requires O(n) work thus O(n! * n)
            return 

        for i in range(len(arr)):

            # skip if we get the same element
            if arr[i] in currPermute:
                continue 

            currPermute.append(arr[i])

            self.backTrack(arr, currPermute, result)

            currPermute.pop()
        
        return result

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