import unittest
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # edge case:
        if len(nums) == 1:
            return True
        
        if nums[0] == 0:
            return False # can jump
        
        # greedy interation
        leastJumps = len(nums) - 1 
        for i in range(len(nums)):
            currIndex = i

            while currIndex < leastJumps and nums[nums[currIndex + i]] != 0 and currIndex != leastJumps:
                if nums[nums[currIndex]] + nums[currIndex] >= leastJumps:
                    return True
                currIndex = nums[currIndex]

        return False

class TestJumpGame(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    # def test_reachable(self):
    #     nums = [2,3,1,1,4]
    #     self.assertTrue(self.solution.canJump(nums))

    def test_unreachable(self):
        nums = [3,2,1,0,4]
        self.assertFalse(self.solution.canJump(nums))

    # def test_single_element(self):
    #     nums = [0]
    #     self.assertTrue(self.solution.canJump(nums))

    # def test_large_jump(self):
    #     nums = [5,4,3,2,1,0,0,0,0,1]
    #     self.assertFalse(self.solution.canJump(nums))

    # def test_always_zero(self):
    #     nums = [0,0,0,0]
    #     self.assertFalse(self.solution.canJump(nums))

if __name__ == "__main__":
    unittest.main()
