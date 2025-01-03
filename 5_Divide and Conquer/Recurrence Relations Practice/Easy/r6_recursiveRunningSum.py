from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        """return running sum"""

        # Problem can be easily solved in Time complexity O(n) and 
        # Space Complexity of O(1) but we will practice recursion with this
        # solution

        # Base/Termination Case:
        if len(nums) <= 1:
            return nums
        
        # Division phase:
        mid = len(nums) // 2
        leftArr = self.runningSum(nums[:mid])
        rightArr = self.runningSum(nums[mid:])

        # Conquer and Combine Phase
        return self.returnSum(leftArr, rightArr)
    
    def returnSum(self, leftArr, rightArr):
        """Calc. sum for respective index"""

        currIndex = 0
        while currIndex < len(rightArr):
            rightArr[currIndex] += leftArr[-1]
            currIndex += 1

        return leftArr + rightArr

# Recurrence relations: T(n) = 2T(n / 2) + T(n / 2) + O(1) # Time Complexity O(n log n) and Space Complexity O(log n)

	# •	Each level of recursion involves O(n) work to combine the results.
	# •	There are \log n levels of recursion due to halving the array at each step.
	# •	Total work: O(n) \times O(\log n) = O(n \log n).


sol = Solution()
print(sol.runningSum([1,2,3,4])) # Expected Output: [1,3,6,10]
print(sol.runningSum([1,1,1,1,1])) # Expected Output: [1,2,3,4,5]
print(sol.runningSum([3,1,2,10,1])) # Expected Output: [3,4,6,16,17]