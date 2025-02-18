from typing import List
import unittest

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        return power set of provided set
        Time complexity: O(n * n^2) and space complexity: O(h)
        """
        
        def exploreSet(set, index, subset):
            """return subsets"""

            if len(nums) == index:
                self.result.append(subset[:]) # Add to result
                return 
            
            # Exlusive of current element
            exploreSet(set, index + 1, subset)

            # Inclusive of current element
            subset.append(set[index])
            exploreSet(set, index + 1, subset)

            # Backtrack
            subset.pop()

        self.result = []
        exploreSet(nums, 0, [])
        return self.result
    
    def ApproachSolution(self):
        """
        To find all the powerset in the input array, the approach to this problem
        will require exhaustive search which is perfect for a backtracking approach

        first, write a backtracking algorithm with arguments that includes an empty array 
        for potential sets, the input array and index initialized at 0.

        Our base condition for this approach will be to take a copy of or current set
        if index is equal to the length of our input array then return

        From here we take two approaches for the recursion, the exclusive approach where
        we decide not to add the current value of our input array and then our inclusive 
        approach were we add the current value

        On return we backtrack track by poping last add val in our subset

        At end of recursion we should have all powersets to return as our result

        Time Complexity: O(n * 2^n), we explore each value and decide make a choice if we should add or not --> 2^n
        Space Complexity: No auxillary DS used except for recursion O(h) 
        """

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

    # def test_example2(self):
    #     nums = [0]
    #     expected_output = [
    #         [], [0]
    #     ]
    #     self.assertCountEqual(self.solution.subsets(nums), expected_output)

    # def test_empty_input(self):
    #     nums = []
    #     expected_output = [
    #         []
    #     ]
    #     self.assertCountEqual(self.solution.subsets(nums), expected_output)

    # def test_large_input(self):
    #     nums = [1, 2, 3, 4]
    #     # Expected output contains all subsets of nums
    #     expected_output = [
    #         [], [1], [2], [3], [4],
    #         [1, 2], [1, 3], [1, 4],
    #         [2, 3], [2, 4], [3, 4],
    #         [1, 2, 3], [1, 2, 4], [1, 3, 4],
    #         [2, 3, 4], [1, 2, 3, 4]
    #     ]
    #     self.assertCountEqual(self.solution.subsets(nums), expected_output)

    # def test_negative_numbers(self):
    #     nums = [-1, -2, -3]
    #     expected_output = [
    #         [], [-1], [-2], [-3],
    #         [-1, -2], [-1, -3], [-2, -3],
    #         [-1, -2, -3]
    #     ]
    #     self.assertCountEqual(self.solution.subsets(nums), expected_output)

    # def test_mixed_numbers(self):
    #     nums = [-1, 0, 1]
    #     expected_output = [
    #         [], [-1], [0], [1],
    #         [-1, 0], [-1, 1], [0, 1],
    #         [-1, 0, 1]
    #     ]
    #     self.assertCountEqual(self.solution.subsets(nums), expected_output)

if __name__ == "__main__":
    unittest.main()