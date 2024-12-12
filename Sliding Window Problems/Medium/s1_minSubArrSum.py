from typing import List

# Time Complexity O(n), Space Complexity O(1) - Completed in 20 minutes
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        return min subarray length were it's sum => target
        """

        # Initialize variables
        minLenArr = float('inf')
        leftIndex = 0
        arrLen = len(nums)
        currSum = 0

        # iterate through right index
        for rightIndex in range(arrLen):
            currSum += nums[rightIndex]

            # control desired window size through left index
            while currSum >= target:
                minLenArr = min(minLenArr, rightIndex - leftIndex + 1)

                # drop curr leftIndex val before iterating 
                currSum -= nums[leftIndex]
                leftIndex += 1
        
        return 0 if minLenArr == float('inf') else minLenArr
    
sol = Solution()
print(sol.minSubArrayLen(7, [2,3,1,2,4,3])) #Expected: 2
print(sol.minSubArrayLen(11, [1,1,1,1,1,1,1,1])) #Expected: 0
print(sol.minSubArrayLen(7, [5])) #Expected: 0
print(sol.minSubArrayLen(7, [10, 2, 3])) #Expected: 1

# Time complexity O(n^2) SC O(1)
# First medium problem solved but inefficient - Took about 90 minutes
# class Solution:
#     def minSubArrayLen(self, target: int, nums: List[int]) -> int:
#         """
#         return min subarray length were a sum => target
#         """

#         # establish base variables
#         arrLen = len(nums)
#         leftIndex, rightIndex = 0, 1
#         minLenArr = float('inf') 

#         if arrLen == 1:
#             return 1 if nums[0] >= target else 0

#         if nums[leftIndex] >= target or nums[rightIndex] >= target:
#             return 1 # 1 is the min length we can find (so we can stop calc. early)
        
#         sumWindow = sum(nums[leftIndex:rightIndex + 1]) # rightIndex is inclusive
#         windowLength = len(nums[leftIndex : rightIndex + 1])
        
#         while rightIndex < arrLen and minLenArr > 1:         
#             if sumWindow == target:
#                 minLenArr = min(minLenArr, windowLength)
#                 if rightIndex != arrLen -1:
#                     sumWindow = sumWindow - nums[leftIndex] + nums[rightIndex + 1]
#                 else:
#                     sumWindow = sumWindow - nums[leftIndex] + nums[rightIndex]
#                 rightIndex += 1
#                 leftIndex += 1
                

#             elif sumWindow > target:
#                 minLenArr = min(minLenArr, windowLength)
#                 sumWindow -= nums[leftIndex]
#                 leftIndex += 1
#                 windowLength -= 1

#             elif sumWindow < target:
#                 rightIndex += 1
#                 if rightIndex <= arrLen - 1:
#                     sumWindow += nums[rightIndex] 
#                     windowLength += 1
            
#         return 0 if minLenArr == float('inf') else minLenArr

