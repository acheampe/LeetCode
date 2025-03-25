import unittest

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        """
        return the longest sebsequence in input nums
        """
        
        countSubSequence = [1] * len(nums)
        
        for i in range(len(nums)):
            for j in range(i):
                
                if nums[j] < nums[i]:
                    countSubSequence[i] = max(countSubSequence[j] + 1, countSubSequence[i])
        
        return max(countSubSequence)
        

class TestSolution(unittest.TestCase):
    def test_lengthOfLIS(self):
        sol = Solution()
        
        # Basic test cases
        self.assertEqual(sol.lengthOfLIS([10,9,2,5,3,7,101,18]), 4)
        self.assertEqual(sol.lengthOfLIS([0,1,0,3,2,3]), 4)
        self.assertEqual(sol.lengthOfLIS([7,7,7,7,7,7,7]), 1)

        # Edge cases
        self.assertEqual(sol.lengthOfLIS([1]), 1)  # Single element
        self.assertEqual(sol.lengthOfLIS([10,20,30,40]), 4)  # Already increasing
        self.assertEqual(sol.lengthOfLIS([4,10,4,3,8,9]), 3)  # Random sequence
        
        # Large input case
        self.assertEqual(sol.lengthOfLIS(list(range(2500))), 2500)  # Strictly increasing

if __name__ == "__main__":
    unittest.main()