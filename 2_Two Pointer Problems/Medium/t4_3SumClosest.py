from typing import List

# TC O(n^2); O(1)
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """return sum of three integers closest to target"""

        priorClosestDiff = None
        nums.sort() # TC O (n log n)

        for i in range(len(nums)):
            
            if i + 1 == len(nums):
                continue

            fixedVal = nums[i]
            startIndex = i + 1
            endIndex = len(nums) - 1

            while startIndex < endIndex:
                currTotal = fixedVal + nums[startIndex] + nums[endIndex]
                
                if priorClosestDiff == None:
                    currClosestDiff = abs(currTotal - target)
                    priorClosestDiff = currClosestDiff
                    result = currTotal
            
                else:
                    currClosestDiff = abs(currTotal - target)
                    ClosestDiff = min(currClosestDiff, priorClosestDiff)
                    
                    if ClosestDiff == currClosestDiff:
                        result = currTotal
                        priorClosestDiff = currClosestDiff
                
                if currTotal < target:
                    startIndex +=1
                
                else:
                    endIndex -= 1
        
        return result 
    
sol = Solution()
print(sol.threeSumClosest([-1,2,1,-4], 1)) # Expected: 2
print(sol.threeSumClosest([0,0,0], 1)) # Expected: 0
print(sol.threeSumClosest([4,0,5,-5,3,3,0,-4,-5], -2)) # Expected: -2

### EASIER TO READ VARIANT ###
# from typing import List

# class Solution:
#     def threeSumClosest(self, nums: List[int], target: int) -> int:
#         """Return the sum of three integers closest to the target."""
#         nums.sort()  # Sort the array to apply two-pointer logic
#         closestSum = float('inf')  # Initialize to a very large value
        
#         for i in range(len(nums) - 2):  # We need at least three values
#             startIndex, endIndex = i + 1, len(nums) - 1
            
#             while startIndex < endIndex:
#                 currTotal = nums[i] + nums[startIndex] + nums[endIndex]
                
#                 # Update the closest sum if this one is better
#                 if abs(currTotal - target) < abs(closestSum - target):
#                     closestSum = currTotal
                
#                 # Move pointers based on comparison to the target
#                 if currTotal < target:
#                     startIndex += 1
#                 else:
#                     endIndex -= 1
        
#         return closestSum


