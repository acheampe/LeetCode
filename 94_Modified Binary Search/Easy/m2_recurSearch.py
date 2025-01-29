from typing import List
import unittest

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Performs binary search on a sorted list to find the target index.

        Args:
            nums (List[int]): Sorted list of integers.
            target (int): The integer to search for.

        Returns:
            int: The index of the target in nums, or -1 if not found.

        Time Complexity: O(log n)
        Space Complexity: O(log n) for recursive stack
        """

        def recursiveSearch(left, right):
            
            # edge case:
            if left > right:
                return - 1
            
            mid = left + ((right - left) // 2)

            if nums[mid] == target:
                return mid
            
            elif nums[mid] > target:
                return recursiveSearch(left, mid - 1)
            
            else: 
                return recursiveSearch(mid + 1, right) 

        return recursiveSearch(0, len(nums) - 1)

        



class TestSearch(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()
    
    def test_target_at_middle(self):
        nums = [-1, 0, 3, 5, 9, 12]
        target = 9
        expectedOutput = 4
        self.assertEqual(self.sol.search(nums, target), expectedOutput)

    def test_target_not_found(self):
        nums = [-1, 0, 3, 5, 9, 12]
        target = 2
        expectedOutput = -1
        self.assertEqual(self.sol.search(nums, target), expectedOutput)

    def test_target_at_beginning(self):
        nums = [-1, 0, 3, 5, 9, 12]
        target = -1
        expectedOutput = 0
        self.assertEqual(self.sol.search(nums, target), expectedOutput)

    def test_target_at_end(self):
        nums = [-1, 0, 3, 5, 9, 12]
        target = 12
        expectedOutput = 5
        self.assertEqual(self.sol.search(nums, target), expectedOutput)

    def test_single_element_found(self):
        nums = [7]
        target = 7
        expectedOutput = 0
        self.assertEqual(self.sol.search(nums, target), expectedOutput)

    def test_single_element_not_found(self):
        nums = [7]
        target = 3
        expectedOutput = -1
        self.assertEqual(self.sol.search(nums, target), expectedOutput)

    def test_even_sized_array_target_found(self):
        nums = [2, 4, 6, 8, 10, 12]
        target = 6
        expectedOutput = 2
        self.assertEqual(self.sol.search(nums, target), expectedOutput)

    def test_even_sized_array_target_not_found(self):
        nums = [2, 4, 6, 8, 10, 12]
        target = 5
        expectedOutput = -1
        self.assertEqual(self.sol.search(nums, target), expectedOutput)

    def test_odd_sized_array_target_found(self):
        nums = [1, 3, 5, 7, 9]
        target = 7
        expectedOutput = 3
        self.assertEqual(self.sol.search(nums, target), expectedOutput)

    def test_odd_sized_array_target_not_found(self):
        nums = [1, 3, 5, 7, 9]
        target = 6
        expectedOutput = -1
        self.assertEqual(self.sol.search(nums, target), expectedOutput)

    def test_large_array_target_found(self):
        nums = list(range(-10**4, 10**4, 2))  # Even numbers from -10^4 to 10^4
        target = 100
        expectedOutput = nums.index(target)
        self.assertEqual(self.sol.search(nums, target), expectedOutput)

    def test_large_array_target_not_found(self):
        nums = list(range(-10**4, 10**4, 2))  # Even numbers from -10^4 to 10^4
        target = 101  # Odd number, should not be found
        expectedOutput = -1
        self.assertEqual(self.sol.search(nums, target), expectedOutput)


if __name__ == "__main__":
    unittest.main()