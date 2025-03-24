
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        """
        return list[int] with max val of window k of sliding window.
        TC: O(n)
        SC: O(k) at worst
        """

        # establish monotonic stack (decreasing) and return result array
        maxResult = []
        monoStack = deque() # SC ast most O(k) size

        for i in range(len(nums)):

            startWindowIndex = (i - k + 1)

            # check to see if current window in monoStack is still valid
            if monoStack and monoStack[0] < startWindowIndex:
                monoStack.popleft() # no longer valid
            
            while monoStack and nums[i] > nums[monoStack[-1]]:
                # to maintain decreasing order
                monoStack.pop()
        
            # append index to maintain decreasing monotonic order
            monoStack.append(i)

            if i >= k - 1: # only add to max list after initial valid window has been explored
                maxResult.append(nums[monoStack[0]])
        
        return maxResult
        
sol = Solution()
print(sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)) # Expected [3,3,5,5,6,7]
print(sol.maxSlidingWindow([1], 1)) # Expected [1]
print(sol.maxSlidingWindow([1,3,1,2,0,5], 3)) # Expected [3,3,2,5]
print(sol.maxSlidingWindow([1, -1], 1)) # Expected [1, -1]
print(sol.maxSlidingWindow([-7,-8,7,5,7,1,6,0], 4)) # Expected [7,7,7,7,7]
print(sol.maxSlidingWindow([1,-9,8,-6,6,4,0,5], 4)) # Expected [8,8,8,6,6]