from typing import List

# Best complexity for 3SUM is O(n^2), SC O(1) if using two pointer + sort
# For 4SUM, TC is O(n^3)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
        Notice that the solution set must not contain duplicate triplets.
        """
        result = []
        nums.sort() # To ease ability to handle duplicates = O(n Log n)     

        for i in range(len(nums)):
            # Handle fixed index duplicate
            if i > 0 and nums[i] == nums[i-1]:
                continue #iterate to the next index (ignore or conditions below)

            fixedVal = nums[i]
            startIndex = i + 1
            endIndex = len(nums) - 1

            while startIndex < endIndex:
                
                totalVal = nums[startIndex] + nums[endIndex] + fixedVal
                if totalVal == 0:
                    result.append([nums[startIndex], nums[endIndex], fixedVal])
                
                    while startIndex < endIndex and nums[endIndex] == nums[endIndex - 1]:
                        endIndex -= 1 # To avoid duplicate calc

                    while startIndex < endIndex and nums[startIndex] == nums[startIndex + 1]:
                        startIndex += 1 # To avoid duplicates calc
                    
                    startIndex += 1
                    endIndex -=1
                
                elif totalVal < 0:
                    startIndex += 1

                else:
                    endIndex -= 1
            
        return result


sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4])) # Expected: [[-1,-1,2],[-1,0,1]]
print(sol.threeSum([0,1,1])) # Expected: []
print(sol.threeSum([0,0,0])) # Expected: [[0,0,0]]
print(sol.threeSum([3,-2,1,0])) # Expected: []
print(sol.threeSum([1,-1,0])) # Expected: [[-1,0,1]]
print(sol.threeSum([1,2,-2,-1])) # Expected: []
print(sol.threeSum([1,-1,-1,0])) # Expected: [[-1,0,1]]
print(sol.threeSum([-2,0,1,1,2])) # Expected: [[-2,0,2],[-2,1,1]]


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