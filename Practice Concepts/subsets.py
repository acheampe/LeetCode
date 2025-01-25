from typing import List
import unittest

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        return the power set of input arr
        """
        def backtracking(arrSet, subSet, index, result):
            """
            explore and return all valid subsets
            Time complexity: O(n * 2^n)
            space Complexity: O(h), Avg case: O(log n) if tree is balanced
            """
            # Set up a return condition
            if index == len(arrSet):
                result.append(subSet[:])
                return
            
            # Don't include currElement
            backtracking(arrSet, subSet, index + 1, result)

            # Include currElement
            subSet.append(arrSet[index])
            backtracking(arrSet, subSet, index + 1, result)

            # backtrack
            subSet.pop()
        
        result = []
        backtracking(nums, [], 0, result)

        return result
    
class TestSubsets(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        nums = [1, 2, 3]
        expected_output = [
            [], [1], [2], [3],
            [1, 2], [1, 3], [2, 3],
            [1, 2, 3]
        ]
        self.assertCountEqual(self.solution.subsets(nums), expected_output)

    def test_example2(self):
        nums = [0]
        expected_output = [
            [], [0]
        ]
        self.assertCountEqual(self.solution.subsets(nums), expected_output)

    def test_empty_input(self):
        nums = []
        expected_output = [
            []
        ]
        self.assertCountEqual(self.solution.subsets(nums), expected_output)

    def test_large_input(self):
        nums = [1, 2, 3, 4]
        # Expected output contains all subsets of nums
        expected_output = [
            [], [1], [2], [3], [4],
            [1, 2], [1, 3], [1, 4],
            [2, 3], [2, 4], [3, 4],
            [1, 2, 3], [1, 2, 4], [1, 3, 4],
            [2, 3, 4], [1, 2, 3, 4]
        ]
        self.assertCountEqual(self.solution.subsets(nums), expected_output)

    def test_negative_numbers(self):
        nums = [-1, -2, -3]
        expected_output = [
            [], [-1], [-2], [-3],
            [-1, -2], [-1, -3], [-2, -3],
            [-1, -2, -3]
        ]
        self.assertCountEqual(self.solution.subsets(nums), expected_output)

    def test_mixed_numbers(self):
        nums = [-1, 0, 1]
        expected_output = [
            [], [-1], [0], [1],
            [-1, 0], [-1, 1], [0, 1],
            [-1, 0, 1]
        ]
        self.assertCountEqual(self.solution.subsets(nums), expected_output)

if __name__ == "__main__":
    unittest.main()