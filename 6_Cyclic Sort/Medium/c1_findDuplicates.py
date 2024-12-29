from typing import List

from typing import List

class Solution: # TC = O(n) and SC = O(1) - Cyclic Approach
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
        return all integers that appears at most twice
        """

        n = len(nums)

        # Edge case:
        if n == 1:
            return []
        
        duplicateElements = []

        for i in range(n):

            # Concern addressed: Use Cyclic Sort
            while nums[i] != i + 1 and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            
        
        # Find duplicate
        for i in range(n):

            if nums[i] != i + 1:
                duplicateElements.append(nums[i]) # a duplicate is found
        
        return duplicateElements

sol = Solution()
# print(sol.findDuplicates([1,1,2]))  # Expected: [1]
# print(sol.findDuplicates([4,3,2,7,8,2,3,1]))  # Expected: [2, 3]
print(sol.findDuplicates([5,4,6,7,9,3,10,9,5,6]))  # Expected: [9,5,6]
# print(sol.findDuplicates([2,1]))  # Expected: []        
