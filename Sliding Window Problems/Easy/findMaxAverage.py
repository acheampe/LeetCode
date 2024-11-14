from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        Returns the max average sum in an array
        Time Complexity O(n)
        Space Complexity (1)
        """

        # Eliminate edge case (len of num v k)
        if k > len(nums):
            print("Invalid - k length greater than length of nums")
            return -1

        # Find currSum of window size
        currSum = sum(nums[:k])

        # Initialize maxSum to currSum
        maxSum = currSum

        # set a loop to iterate through the array
        for i in range(len(nums) - k):
            currSum = currSum - nums[i] + nums[i + k]
            maxSum = max(maxSum, currSum)

        # return maxAvgSum
        return maxSum/k



        