from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """return single NonDuplicate val in sorted arr"""

        # Base Case/Termination case
        if len(nums) <= 1:
            return nums

        # Division phase:
        mid = len(nums) // 2
        compareLeft = self.singleNonDuplicate(nums[:mid])
        compareRight = self.singleNonDuplicate(nums[mid:])

        if compareLeft == None or compareRight == None:
            return compareRight if compareRight != None else compareLeft
    
        # Conquer to find duplicate
        return self.findDuplicate(compareLeft, compareRight)
    
    def findDuplicate(self, leftArr, rightArr):
        """compare right end val to left start val to find NonDuplicate, if none
            return -1
        """
        if leftArr[-1] != rightArr[0]:
            return [leftArr[-1]] if len(rightArr) > 1 and rightArr[0] == rightArr[1] else [leftArr[-1]]

sol = Solution()
print(sol.singleNonDuplicate([1,1,2,3,3,4,4,8,8])) # Expected Output: 2
print(sol.singleNonDuplicate([3,3,7,7,10,11,11])) # Expected Output: 10