from typing import List
from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
        Notice that the solution set must not contain duplicate triplets.
        """

        # Initiate variables
        trackSet = set()
        listResult = []
        sumMap = defaultdict(int)
        leftIndex, rightIndex = 0, 1

        # Map out list of nums
        for _, val in enumerate(nums):
            sumMap[val] += 1
        
        # Two point Iteration
        while rightIndex < len(nums):
            
            #Calc needed value to == 0
            missingVal = 0 - (nums[leftIndex]) - (nums[rightIndex])

            # checks index correspondent to make sure it is unique
            if missingVal in sumMap and sumMap[missingVal] > 0:
                currTuple = (nums[leftIndex], nums[rightIndex], missingVal)
                leftIndex += 1
                rightIndex += 1
                sumMap[missingVal] -= 1

                sortedCurrTuple = tuple(sorted(currTuple))
                if sortedCurrTuple not in trackSet:
                    trackSet.add(sortedCurrTuple)
                    listResult.append(list(sortedCurrTuple))

            else:
                leftIndex += 1
                rightIndex += 1

        return listResult

sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4])) # Expected: [[-1,-1,2],[-1,0,1]]
print(sol.threeSum([0,1,1])) # Expected: []
print(sol.threeSum([0,0,0])) # Expected: [[0,0,0]]
print(sol.threeSum([3,-2,1,0])) # Expected: []