from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        """return running sum"""

        # Problem can be easily solved in Time complexity O(n) and 
        # Space Complexity of O(1)

        currSum = 0

        for i in range(len(nums)):
            currSum += nums[i]
            nums[i] = currSum

        return nums

sol = Solution()
print(sol.runningSum([1,2,3,4])) # Expected Output: [1,3,6,10]
print(sol.runningSum([1,1,1,1,1])) # Expected Output: [1,2,3,4,5]
print(sol.runningSum([3,1,2,10,1])) # Expected Output: [3,4,6,16,17]