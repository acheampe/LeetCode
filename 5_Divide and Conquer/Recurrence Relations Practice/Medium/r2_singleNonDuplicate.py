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
    
        # Conquer and return non-duplicates
        nonDuplicateList = self.findNonDuplicate(compareLeft, compareRight)

        return nonDuplicateList

        
    
    def findNonDuplicate(self, leftArr, rightArr):
        """compare right and left array and return only non-duplicate list
        """

        if len(leftArr) == 1 and len(rightArr) == 1:
            return leftArr + rightArr
        
        elif len(leftArr) == 1 or len(rightArr) == 1:

            singleLenArr = leftArr if len(leftArr) == 1 else rightArr
            twoLenArr = leftArr if len(leftArr) == 2 else rightArr
            
            if twoLenArr[0] == twoLenArr[1]:
                return singleLenArr # leftArr holds the unique val
            
            # return the non-duplicate
            elif singleLenArr[0] == twoLenArr[0] or singleLenArr[0] == twoLenArr[1]:
                return [twoLenArr[1]] if singleLenArr[0] == twoLenArr[0] else [twoLenArr[0]]
        
        else: # Cases where both left and right arrLen = 2

            # Eliminate arr with duplicate
            if leftArr[0] == leftArr[1]:
                return rightArr
            
            elif rightArr[0] == rightArr[1]:
                return leftArr
            
            # create new arr of nonduplicates
            elif rightArr[0] == leftArr[-1]:
                return [leftArr[0], rightArr[1]]
    
# Recurrence relations: T(n) = 2T(n / 2) + O(n) - Time Complexity = n log n and space complexity = n
            

    
            
sol = Solution()
print(sol.singleNonDuplicate([1,1,2,3,3,4,4,8,8])) # Expected Output: 2
print(sol.singleNonDuplicate([3,3,7,7,10,11,11])) # Expected Output: 10