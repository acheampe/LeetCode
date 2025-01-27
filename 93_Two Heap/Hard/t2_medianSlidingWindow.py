from typing import List
import unittest
import heapq
from collections import deque

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        """
        return an array of the median in sliding window k
        Time Complexity: O(n) for iterating through array
        Space Complexity: O(n) heapify array
        """

        # #Establish memory needed for operation
        stackq = deque([]) # contain index values
        result = [] # contain our median values

        # establish iteration:
        for i in range(len(nums)):

            # append to stack
            stackq.append(i)

            # check to see if stackq[0] is not within valid window range
            if stackq and stackq[0] < (i - k + 1): # valid starting window index
                stackq.popleft() # to always make sure stackq.length == k

            # Use Min and Max heap to find median if stackq.length == k
            if stackq and len(stackq) == k:

                largeHeap, smallHeap = [], []

                for i in range(len(stackq)):
                    
                    heapq.heappush(largeHeap, -nums[stackq[i]])

                    # check to make sure head of large is alway atleast == to min
                    # to maintain valid separation
                    if largeHeap and smallHeap and -largeHeap[0] > smallHeap[0]:
                        heapq.heappush(smallHeap, -heapq.heappop(largeHeap))  # log n operation
                    
                    # Make sure length is near equivalent
                    if len(largeHeap) > len(smallHeap) + 1:
                        heapq.heappush(smallHeap, -heapq.heappop(largeHeap))  # log n operation 
                    if  len(smallHeap) > len(largeHeap):
                        heapq.heappush(largeHeap, -heapq.heappop(smallHeap))                      

                result.append(self.findMedian(largeHeap, smallHeap))

        return result
    
    def findMedian(self, largeHeap, smallHeap):
        """
        return median
        """

        if len(largeHeap) > len(smallHeap): # by earlier logic, only largeHeap can be longer if so
            return  -largeHeap[0]
        
        return (-largeHeap[0] + smallHeap[0]) / 2
    

class TestMedianSlidingWindow(unittest.TestCase):
    def test_median_sliding_window(self):
        solution = Solution()
        
        # Test case 1: Example from the problem statement
        nums = [1, 3, -1, -3, 5, 3, 6, 7]
        k = 3
        expected = [1.00000, -1.00000, -1.00000, 3.00000, 5.00000, 6.00000]
        self.assertAlmostEqual(solution.medianSlidingWindow(nums, k), expected, delta=1e-5)

        # Test case 2: Another example from the problem statement
        nums = [1, 2, 3, 4, 2, 3, 1, 4, 2]
        k = 3
        expected = [2.00000, 3.00000, 3.00000, 3.00000, 2.00000, 3.00000, 2.00000]
        self.assertAlmostEqual(solution.medianSlidingWindow(nums, k), expected, delta=1e-5)

        # Test case 3: Single element in the array, window size 1
        nums = [5]
        k = 1
        expected = [5.00000]
        self.assertAlmostEqual(solution.medianSlidingWindow(nums, k), expected, delta=1e-5)

        # Test case 4: All identical elements
        nums = [2, 2, 2, 2, 2]
        k = 2
        expected = [2.00000, 2.00000, 2.00000, 2.00000]
        self.assertAlmostEqual(solution.medianSlidingWindow(nums, k), expected, delta=1e-5)

        # Test case 5: Large array, k = 1
        nums = list(range(1, 1001))
        k = 1
        expected = [float(num) for num in nums]
        self.assertAlmostEqual(solution.medianSlidingWindow(nums, k), expected, delta=1e-5)

        # Test case 6: Large array, k = len(nums)
        nums = [1, 3, 2, 4]
        k = 4
        expected = [2.50000]  # Median of the entire array
        self.assertAlmostEqual(solution.medianSlidingWindow(nums, k), expected, delta=1e-5)

if __name__ == '__main__':
    unittest.main()