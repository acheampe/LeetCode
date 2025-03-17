import unittest
from unittest import result

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        """
        Compute the length of the longest increasing subsequence (LIS).
        DP Approach: Bottom-Up
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        """
        if not nums:
            return 0
        
        # Step 1: Create DP array
        dp = [1] * len(nums)  # Each number is a subsequence of length 1
        
        # Step 2: Build DP table
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:  # If valid increasing sequence
                    dp[i] = max(dp[i], dp[j] + 1)  # Take the longest sequence
        
        # Step 3: Return the longest LIS found
        return max(dp)
                     
        
    
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