from typing import List

class Solution: # TC = O(n) and SC = O(1) - Sign Marking Approach
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
        return all integers that appears at most twice
        """

        n = len(nums)

        # Edge case of single arr:
        if n == 1:
            return []
        
        duplicateElements = []
        
        for i in range(n):

            # Mark corresponding Index
            corrIndex = abs(nums[i]) - 1

            if nums[corrIndex] < 0:
                # It means a similar value has tagged it so append duplicate
                duplicateElements.append(abs(nums[i]))
            
            else:
                nums[corrIndex] = - nums[corrIndex]

        return duplicateElements

sol = Solution()
# print(sol.findDuplicates([1,1,2]))  # Expected: [1]
print(sol.findDuplicates([4,3,2,7,8,2,3,1]))  # Expected: [2, 3]
# print(sol.findDuplicates([5,4,6,7,9,3,10,9,5,6]))  # Expected: [9,5,6]
# print(sol.findDuplicates([2,1]))  # Expected: []        
