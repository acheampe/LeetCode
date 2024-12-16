from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pass

sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4])) # Expected: [[-1,-1,2],[-1,0,1]]
print(sol.threeSum([0,1,1])) # Expected: []
print(sol.threeSum([0,0,0])) # Expected: [[0,0,0]]