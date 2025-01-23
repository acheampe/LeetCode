from typing import List
from collections import deque

# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         """Return the maximum values in each sliding window of size k."""
#         n = len(nums)

#         # Not necassary due to constraints
#         if n * k == 0:  # Edge case: empty nums or k = 0
#             return []
        
#         result = []
#         subWindow = deque()  # Store indices of elements in the current window
        
#         for i in range(n):
#             # Remove indices of elements not in the current window
#             currWindow = i - k + 1
#             if subWindow and subWindow[0] < currWindow:
#                 subWindow.popleft()
            
#             # Remove indices of elements smaller than the current element
#             # (They are useless because they cannot be the max)
#             while subWindow and nums[subWindow[-1]] < nums[i]:
#                 subWindow.pop()
            
#             # Add current element's index to the deque
#             subWindow.append(i)
            
#             # Append the maximum value to the result once the first window is complete
#             if i >= k - 1:
#                 result.append(nums[subWindow[0]])  # Front of the deque is the max
        
#         return result

from typing import List
from collections import defaultdict


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        return the maxVal in a sliding Window of k in nums
        Time Complexity: O(n)  and Space Complexity: O(k), if exclusing the returned result
        """

        # S1: Establish memory needed for most of the operation
        currWindow = defaultdict(int)
        maxVal = float('-inf')
        result = [] 

        # S2: Add val to Current Window
        for i in range(k):
            if not currWindow[nums[i]]:
                currWindow[nums[i]] = 0
            currWindow[nums[i]] += 1

        leftIndex = 0 # for window reduction logic 

        # iterate expansion
        for right in range(k, len(nums)):
            currMax = self.findCurrMax(currWindow, maxVal)
            result.append(currMax)

            if not currWindow[nums[right]]:
                currWindow[nums[right]] = 0
            currWindow[nums[right]] += 1

            # window reduction
            currWindow[nums[leftIndex]] -= 1
            if currWindow[nums[leftIndex]] == 0:
                del currWindow[nums[leftIndex]] # To maintain key at length 3
            leftIndex += 1

        # To consider the last Window
        currMax = self.findCurrMax(currWindow, maxVal)
        result.append(currMax)
        return result 

    def findCurrMax(self, currWindow, currMaxVal):
        """
        return current MaxVal
        """

        # length of key should always be 3
        # space operation here: O(k)
        for key in currWindow.keys():
            currMaxVal = max(currMaxVal, key)
        
        return currMaxVal


sol = Solution()
print(sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)) # Expected [3,3,5,5,6,7]
print(sol.maxSlidingWindow([1], 1)) # Expected [1]
print(sol.maxSlidingWindow([1,3,1,2,0,5], 3)) # Expected [3,3,2,5]
print(sol.maxSlidingWindow([1, -1], 1)) # Expected [1, -1]
print(sol.maxSlidingWindow([-7,-8,7,5,7,1,6,0], 4)) # Expected [7,7,7,7,7]
print(sol.maxSlidingWindow([1,-9,8,-6,6,4,0,5], 4)) # Expected [8,8,8,6,6]