from typing import List
from collections import deque, defaultdict


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """return the maxVal in a sliding Window of k in nums"""

        subWindow = deque()
        mapVal = defaultdict(int)
        maxVal = float('-inf')

        # Calc. initial window + initial sum
        for i in range(len(nums[:k])):
            subWindow.append(nums[i])
            mapVal[nums[i]] += 1
            maxVal = max(maxVal, nums[i])
        
        # Track curr maxval
        result = [maxVal]

        
        for i in range(k, len(nums)):

            removeVal = subWindow.popleft()
            mapVal[removeVal] -= 1
            mapVal[nums[i]] += 1

            if len(subWindow) == 0:
                subWindow.append(nums[i])

            if removeVal == maxVal and mapVal[maxVal] == 0:
                del mapVal[maxVal]
                maxVal = max(subWindow[0], subWindow[-1])
                subWindow.append(nums[i])
                maxVal = max(mapVal.keys())
                result.append(maxVal)
            
            else:
                subWindow.append(nums[i])
                maxVal = max(maxVal, subWindow[-1])
                result.append(maxVal)
        
        return result





sol = Solution()
print(sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)) # Expected [3,3,5,5,6,7]
print(sol.maxSlidingWindow([1], 1)) # Expected [1]
print(sol.maxSlidingWindow([1,3,1,2,0,5], 3)) # Expected [3,3,2,5]
print(sol.maxSlidingWindow([1, -1], 1)) # Expected [1, -1]
print(sol.maxSlidingWindow([-7,-8,7,5,7,1,6,0], 4)) # Expected [7,7,7,7,7]
print(sol.maxSlidingWindow([1,-9,8,-6,6,4,0,5], 4)) # Expected [8,8,8,6,6]