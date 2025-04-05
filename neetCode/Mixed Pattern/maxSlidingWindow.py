from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        decMonoStack = deque() # SC O(k)
        resultArr = [] 

        for i in range(len(nums)): # TC O(n)

            # validate window
            if decMonoStack and decMonoStack[0] < (i - k + 1):
                decMonoStack.popleft()
        
            # Maintain decrease monotonic order
            while decMonoStack and nums[decMonoStack[-1]] < nums[i]:
                decMonoStack.pop()
            
            # Add current index
            decMonoStack.append(i)

            # add to result arr if condition allows
            if (i + 1) - k > -1:
                resultArr.append(nums[decMonoStack[0]])

        return resultArr

sol = Solution()
# print(sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)) # Expected [3,3,5,5,6,7]
# print(sol.maxSlidingWindow([1], 1)) # Expected [1]
# print(sol.maxSlidingWindow([1,3,1,2,0,5], 3)) # Expected [3,3,2,5]
# print(sol.maxSlidingWindow([1, -1], 1)) # Expected [1, -1]
# print(sol.maxSlidingWindow([-7,-8,7,5,7,1,6,0], 4)) # Expected [7,7,7,7,7]
# print(sol.maxSlidingWindow([1,-9,8,-6,6,4,0,5], 4)) # Expected [8,8,8,6,6]
print(sol.maxSlidingWindow([1,3,1,2,0,5], 3)) # Expected [3,3,2,5]