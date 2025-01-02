from typing import List

# Best complexity for 3SUM is O(n^2), SC O(1) if using two pointer + sort
# For 4SUM, TC is O(n^3)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """return all triplets that sum up to 0 in a given array"""

        result = []
        nums.sort()

        for i in range(len(nums)): # fixed point iteration
            if i > 0 and nums[i] == nums[i - 1]:
                continue # to ignore duplicate - IMPORTANT EDGE CASE THAT I FORGOT TO IMPLEMENT - It works because of the sorting done earlier

            j = i + 1
            k = len(nums) - 1

            while j < k:

                if nums[i] + nums[j] + nums[k] == 0:
                    result.append([nums[i], nums[j], nums[k]])

                    # To avoid duplicates
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1

                    j += 1
                    k -= 1
                
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                
                else: 
                    # If total is less than zero
                    j += 1 

        return result




sol = Solution()
# print(sol.threeSum([-1,0,1,2,-1,-4])) # Expected: [[-1,-1,2],[-1,0,1]]
# print(sol.threeSum([0,1,1])) # Expected: []
print(sol.threeSum([0,0,0])) # Expected: [[0,0,0]]
# print(sol.threeSum([3,-2,1,0])) # Expected: []
# print(sol.threeSum([1,-1,0])) # Expected: [[-1,0,1]]
# print(sol.threeSum([1,2,-2,-1])) # Expected: []
# print(sol.threeSum([1,-1,-1,0])) # Expected: [[-1,0,1]]
# print(sol.threeSum([-2,0,1,1,2])) # Expected: [[-2,0,2],[-2,1,1]]


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