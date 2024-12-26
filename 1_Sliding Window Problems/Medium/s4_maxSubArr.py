from typing import List

class Solution: # Utilizing Kadane's Algorithm - where you continuously decide 
    # whether to extend current subarray or to reset it based on evaluation condition (Not a typical expanding and reducing window technique)
    def maxSubArray(self, nums: List[int]) -> int: #TC == O(n) and SC == O(1)
        """
        Find max subarray with largest sum and return the sum
        """

        # Initial Variables
        maxSum = float('-inf')  # Ensure we handle all-negative arrays
        currSum = 0  # Current subarray sum
        
        for num in nums:
            currSum += num

            # Update maxSum with the current sum
            maxSum = max(maxSum, currSum)

            # Reset currSum if it's less than 0
            if currSum < 0:
                currSum = 0
        
        return maxSum

# Test Cases
sol = Solution()
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # Expected: 6
print(sol.maxSubArray([1]))  # Expected: 1
print(sol.maxSubArray([5,4,-1,7,8]))  # Expected: 23
print(sol.maxSubArray([-1]))  # Expected: -1
print(sol.maxSubArray([-2,-1]))  # Expected: -1
