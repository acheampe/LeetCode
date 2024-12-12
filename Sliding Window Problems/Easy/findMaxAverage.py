from typing import List

# class Solution:
#     def findMaxAverage(self, nums: List[int], k: int) -> float:
#         """
#         Return max average of k window in an array
#         """
        
#         arrLen = len(nums)

#         if k > arrLen:
#             print(f'Invalid: {k} value greater than length of array --> {nums}')
        
#         # Calc. val of current window
#         currVal = sum(nums[i] for i in range(0, k, 1))

#         maxVal = currVal

#         # iterate using window to find max average
#         for i in range (1, arrLen - k + 1):
            
#             # calc next iterative sum 
#             dropVal = nums[i - 1]
#             addVal = nums[k + i -1]

#             currVal -= dropVal
#             currVal += addVal

#             maxVal = max(currVal, maxVal)
        
#         return maxVal / k 

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        return the max average of the window within arr
        """

        # Initialize length of Arr
        arrLen = len(nums)

        # Edge case:
        if k > arrLen:
            print("Invalid input")
            return -1
        
        # Initialize Vals
        currVal = sum(nums[:k])
        maxVal = currVal

        # Iterate to find max
        for i in range(1, arrLen - k + 1): # +1 because end val is not inclusive during iteration, and we want to make sure to calc the last window

            dropVal = nums[i - 1]
            addVal = nums[(i - 1) + k]
            
            currVal = currVal - dropVal + addVal

            maxVal = max(currVal, maxVal)

        # return average
        return maxVal / k

        

sol = Solution()
first = sol.findMaxAverage([0,1,1,3,3], 4)
print(first)


        