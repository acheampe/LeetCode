from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """Return the maximum values in each sliding window of size k."""
        n = len(nums)

        # Not necassary due to constraints
        if n * k == 0:  # Edge case: empty nums or k = 0
            return []
        
        result = []
        subWindow = deque()  # Store indices of elements in the current window
        
        for i in range(n):
            # Remove indices of elements not in the current window
            currWindow = i - k + 1
            if subWindow and subWindow[0] < currWindow:
                subWindow.popleft()
            
            # Remove indices of elements smaller than the current element
            # (They are useless because they cannot be the max)
            while subWindow and nums[subWindow[-1]] < nums[i]:
                subWindow.pop()
            
            # Add current element's index to the deque
            subWindow.append(i)
            
            # Append the maximum value to the result once the first window is complete
            if i >= k - 1:
                result.append(nums[subWindow[0]])  # Front of the deque is the max
        
        return result



sol = Solution()
print(sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)) # Expected [3,3,5,5,6,7]
print(sol.maxSlidingWindow([1], 1)) # Expected [1]
# print(sol.maxSlidingWindow([1,3,1,2,0,5], 3)) # Expected [3,3,2,5]
# print(sol.maxSlidingWindow([1, -1], 1)) # Expected [1, -1]
# print(sol.maxSlidingWindow([-7,-8,7,5,7,1,6,0], 4)) # Expected [7,7,7,7,7]
# print(sol.maxSlidingWindow([1,-9,8,-6,6,4,0,5], 4)) # Expected [8,8,8,6,6]