from typing import List
from collections import defaultdict

# Best complexity for 3SUM is O(n^2), SC O(1) if using two pointer + sort
# For 4SUM, TC is O(n^3)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
        Notice that the solution set must not contain duplicate triplets.
        """
        # Sort nums to optimize two pointer usage
        nums.sort()
        resultList = []
        
        for i in range(len(nums)):
            # Skip duplicate fixed elements to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            fixed_num = nums[i]
            rightIndex = len(nums) - 1
            leftIndex = i + 1
            
            while leftIndex < rightIndex:
                
                threeSum = fixed_num + nums[leftIndex ]+ nums[rightIndex]

                if threeSum == 0:
                    resultList.append([fixed_num, nums[leftIndex], nums[rightIndex]])
                
                    #iterate points while skipping duplicates
                    while leftIndex < rightIndex and nums[leftIndex] == nums[leftIndex + 1]:
                        leftIndex += 1
                    
                    while leftIndex < rightIndex and nums[rightIndex] == nums[rightIndex -1]:
                        rightIndex -= 1

                    leftIndex += 1
                    rightIndex -= 1
                
                elif threeSum < 0:
                    leftIndex += 1
                
                else:
                    rightIndex -= 1
                
        return resultList

sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4])) # Expected: [[-1,-1,2],[-1,0,1]]
print(sol.threeSum([0,1,1])) # Expected: []
print(sol.threeSum([0,0,0])) # Expected: [[0,0,0]]
print(sol.threeSum([3,-2,1,0])) # Expected: []
print(sol.threeSum([1,-1,0])) # Expected: [[-1,0,1]]

#########################################
### Complexity Explanation:
# Fixing One Index (i):Fixing One Index (i):
# Two-Pointer Search (Start and End):
## For each fixed index i, the two pointers (start and end) will traverse the remaining
## elements (approximately n−i).
# This traversal is O(n) because each pointer moves once per iteration (no backtracking
# Total Time Complexity:
# Combining the two steps:
## O(n)(outer loop)×O(n)(two pointers)=O(n^2)
###########################################