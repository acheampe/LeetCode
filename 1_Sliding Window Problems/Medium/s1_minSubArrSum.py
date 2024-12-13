from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        return min length of subarray whose sum >= target
        """

        #initiating basic variables
        minLenSubArr = float('inf')
        currSum = 0
        leftIndex = 0

        # Iterate through rightIndex if currSum < target
        for rightIndex in range(len(nums)):
            currSum += nums[rightIndex]

            while currSum >= target:
                minLenSubArr = min(minLenSubArr, rightIndex - leftIndex + 1)

                currSum -= nums[leftIndex]
                leftIndex += 1
        
        return 0 if minLenSubArr == float('inf') else minLenSubArr

        # Time complexity should be: O(n) Space Complexity should be O(1)
        # Completed in 7 minutes and 38 seconds
    
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


