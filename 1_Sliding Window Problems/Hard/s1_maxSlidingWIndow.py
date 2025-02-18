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
        dequeStack = deque()
        maxValues = []

        for i in range(len(nums)):

            # Make sure we are in valid sliding window range:
            if dequeStack and dequeStack[0] < i - k + 1: # for a valid starting window range
                dequeStack.popleft() # no longer in valid window range
            
            # To maintain a decreasing monotonic order
            while dequeStack and nums[dequeStack[-1]] < nums[i]:
                dequeStack.pop()
            
            # Append current in monotonic order
            dequeStack.append(i)

            # only append after we have iterated through atleast our first window
            if i >= k - 1:
                maxValues.append(nums[dequeStack[0]])
        
        return maxValues
    
    def approachSummary(self):
        """
        NOTE: I interchanged stack with the DS deque in my explanation

        This hard problem is a great example of separating difficult problems into 
        smaller areas of concern.

        The first thing to take care of is establishing the data structure needed
        to solve this problem, a monotonic stack (decreasing) and an array to
        return our result

        we initiate a for loop through our input array and then seperate our problem
        into 3 seperate concerns. 

        1) First if stack is True and is the value of our current index greater than
        value of the index at our stack[0], if so update to maintain monotonic decreasing 
        order while marking it as our pointer to our current maxVal 

        2) if stack, does the last pointer to the value of our input array less than the current value
        /pointer to the value that we are looking at. If so, pop stack and append current iterative pointer

        3) add to stack if not stack if above conditions are not met

        4) Create a condition that to start adding to result array from stack[0] when 
        we have at least iterated through our first window.

        Time Complexity = O(n)
        Space Complexity = O(k)
        """


sol = Solution()
print(sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)) # Expected [3,3,5,5,6,7]
print(sol.maxSlidingWindow([1], 1)) # Expected [1]
print(sol.maxSlidingWindow([1,3,1,2,0,5], 3)) # Expected [3,3,2,5]
print(sol.maxSlidingWindow([1, -1], 1)) # Expected [1, -1]
print(sol.maxSlidingWindow([-7,-8,7,5,7,1,6,0], 4)) # Expected [7,7,7,7,7]
print(sol.maxSlidingWindow([1,-9,8,-6,6,4,0,5], 4)) # Expected [8,8,8,6,6]