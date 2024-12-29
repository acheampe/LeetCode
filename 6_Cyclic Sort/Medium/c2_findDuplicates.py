from typing import List

class Solution: # TC = O(n) and SC = O(1) - Sign Marking Approach
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
        return all integers that appears at most twice
        """

        n = len(nums)

        # Edge Case: 
        if n == 1:
            return [] # No duplicates
        
        # variable to catch duplicates
        duplicateElements = []
        
        # Use Sign marking to tease out duplicates - No sorting needed
        # sign marking especially appropriate due to zero indexing
        for i in range(n):
            index = abs(nums[i]) - 1 # Get index that should match value

            if nums[index] < 0:
                duplicateElements.append(abs(nums[i]))
            
            else: # Tag with a negative sign
                nums[index] = -nums[index]


        return duplicateElements

        

sol = Solution()
print(sol.findDuplicates([1,1,2]))  # Expected: [1]
print(sol.findDuplicates([4,3,2,7,8,2,3,1]))  # Expected: [2, 3]
print(sol.findDuplicates([5,4,6,7,9,3,10,9,5,6]))  # Expected: [9,5,6]
print(sol.findDuplicates([2,1]))  # Expected: []        
