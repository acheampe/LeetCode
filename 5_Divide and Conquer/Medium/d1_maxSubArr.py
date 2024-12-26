from typing import List

class Solution: # TC O (n log n)  and SC O (log n) if considering recursive stack
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Find max subarray with largest sum and return the sum
        """

        # Establish Base Case to terminate at:
        if len(nums) <= 1:
            return nums[0]
        
        # Division Phase
        mid = len(nums) // 2
        leftSubArr = self.maxSubArray(nums[:mid])
        rightSubArr = self.maxSubArray(nums[mid:])

        # Conquer Phase: Calc. cross Sum
        leftSum = self.calcCrossingSum(nums, mid, 'left')
        rightSum = self.calcCrossingSum(nums, mid, 'right')

        # Combine Phase: Sum left and right sum
        crossSum = leftSum + rightSum


        return max(crossSum, leftSubArr, rightSubArr)

    def calcCrossingSum(self, arr, mid, direction):
        """
        Calculate the maximum sum of a subarray crossing the midpoint.
        """
        sumTotal = 0
        maxSum = float('-inf')
        
        if direction == 'left':
            for i in range(mid - 1, -1, -1):
                sumTotal += arr[i]
                maxSum = max(maxSum, sumTotal)
        
        else:
            for i in range(mid, len(arr)):
                sumTotal += arr[i]
                maxSum = max(maxSum, sumTotal)

        return maxSum

sol = Solution()
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) # Expected: 6
# print(sol.maxSubArray([1])) # Expected: 1
# print(sol.maxSubArray([5,4,-1,7,8])) # Expected: 23

