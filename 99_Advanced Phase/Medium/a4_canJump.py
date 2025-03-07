import unittest
from typing import List

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Return True if able to reach the last index.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        furthest_index = 0  # Furthest index we can reach
        
        for i in range(len(nums)):
            if i > furthest_index:  # If current index is beyond our reach, return False
                return False
            
            furthest_index = max(furthest_index, i + nums[i])  # Update max reach
            
            if furthest_index >= len(nums) - 1:  # Early exit if we can reach the last index
                return True
        
        return False

class TestJumpGame(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_reachable(self):
        nums = [2,3,1,1,4]
        self.assertTrue(self.solution.canJump(nums))

    def test_unreachable(self):
        nums = [3,2,1,0,4]
        self.assertFalse(self.solution.canJump(nums))

    def test_single_element(self):
        nums = [0]
        self.assertTrue(self.solution.canJump(nums))

    def test_large_jump(self):
        nums = [5,4,3,2,1,0,0,0,0,1]
        self.assertFalse(self.solution.canJump(nums))

    def test_always_zero(self):
        nums = [0,0,0,0]
        self.assertFalse(self.solution.canJump(nums))

if __name__ == "__main__":
    unittest.main()
