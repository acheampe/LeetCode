from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        Return max average of k window in an array
        """
        
        arrLen = len(nums)

        if k > arrLen:
            print(f'Invalid: {k} value greater than length of array --> {nums}')
        
        # Calc. val of current window
        currVal = sum(nums[i] for i in range(0, k, 1))

        maxVal = currVal

        # iterate using window to find max average
        for i in range (1, arrLen - k + 1):
            
            # calc next iterative sum 
            dropVal = nums[i - 1]
            addVal = nums[k + i -1]

            currVal -= dropVal
            currVal += addVal

            maxVal = max(currVal, maxVal)
        
        return maxVal / k 

sol = Solution()
first = sol.findMaxAverage([2,4,6,8,10], 3)
print(first)


        