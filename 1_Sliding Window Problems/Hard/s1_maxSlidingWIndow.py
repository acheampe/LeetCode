from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Return the maximum values in each sliding window of size k
        Time Complexity = O(n)
        Space Complexity = O(k)
        NOTE: This is a great example of seperation of concerns that yields
        desired output
        """

        # Monotonic deque to store indices of elements in decreasing order
        stack = deque()
        maxValues = []

        for i in range(len(nums)):

            # Make sure we are in valid sliding window range:
            if stack and stack[0] < i - k + 1: # for a valid starting window range
                stack.popleft() # no longer in valid window range
            
            # To maintain a decreasing monotonic order
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            
            # Append current in monotonic order
            stack.append(i)

            # only append after we have iterated through atleast our first window
            if i >= k - 1:
                maxValues.append(nums[stack[0]])
        
        return maxValues


sol = Solution()
print(sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)) # Expected [3,3,5,5,6,7]
print(sol.maxSlidingWindow([1], 1)) # Expected [1]
print(sol.maxSlidingWindow([1,3,1,2,0,5], 3)) # Expected [3,3,2,5]
print(sol.maxSlidingWindow([1, -1], 1)) # Expected [1, -1]
print(sol.maxSlidingWindow([-7,-8,7,5,7,1,6,0], 4)) # Expected [7,7,7,7,7]
print(sol.maxSlidingWindow([1,-9,8,-6,6,4,0,5], 4)) # Expected [8,8,8,6,6]