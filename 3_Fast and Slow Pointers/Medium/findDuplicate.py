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
# Optimal Approach:
# TC == O(n) . SC == O(1)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """ 
        return repeated # if solution contains duplicate - there is only one duplicate
        """

        # TC == O(n) SC == O(1)

        # fast and slow pointer initialization
        fastPointer, slowPointer = 0, 0

        # First detect cycle
        while True:
            fastPointer, slowPointer = nums[nums[fastPointer]], nums[slowPointer] # Move fast and slow pointer by 2 and 1 step respectively
            if fastPointer == slowPointer:
                break
        
        # The Find the entry point to return that point
        slowPointer = 0
        while slowPointer != fastPointer:
            slowPointer = nums[slowPointer]
            fastPointer = nums[fastPointer]

        
        return slowPointer

            
sol = Solution()
print(sol.findDuplicate([1,3,4,2,2])) # Expected: 2
print(sol.findDuplicate([3,1,3,4,2])) # Expected: 3
print(sol.findDuplicate([3,3,3,3,3])) # Expected: 3

        
        