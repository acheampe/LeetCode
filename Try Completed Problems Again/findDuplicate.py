# NAIVE APPROACH 1 - O(n log n) SC O(1) #
# To sort array and iterate through arr
# If curr iter == next iter, then return True

# NAIVE APPROACH 2 - O(n) SC O(n) #
# Iterate through arr
# track none duplicate vals in a set == SC O(n)
# if val is in set, return the val. 
# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         """ 
#         return repeated # if solution contains duplicate - there is only one duplicate
#         """

#         # TC == O(n) SC == O(n)
#         inSet = set()

#         for i in range(len(nums)):
#             if nums[i] in inSet:
#                 return nums[i]
#             else:
#                 inSet.add(nums[i])

from typing import List

class Solution: # Acceptable approach if neg sign as visited does not count as modifying arr, else using a fast and slow pointer to detect cycle will do the trick
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Uses neg sign to mark an already parsed val to indicate duplicate
        """

        for i in range(len(nums)):

            val = nums[abs(nums[i])]

            if val < 0:
                return abs(nums[i]) # It means val is already tagged by a duplicate value
            
            else: # tag value with a negative sign to mark explored val
                nums[abs(nums[i])] = -nums[abs(nums[i])]
        
        
        

            
sol = Solution()
print(sol.findDuplicate([1,3,4,2,2])) # Expected: 2
print(sol.findDuplicate([3,1,3,4,2])) # Expected: 3
print(sol.findDuplicate([3,3,3,3,3])) # Expected: 3

        
        