from typing import List
import heapq
from collections import defaultdict
import unittest

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        """
        Returns an array of the median in each sliding window of size k.
        
        Time Complexity: O(n log k) using two heaps.
        Space Complexity: O(k).
        """
        
        # Step 1: Establish memory needed for operation
        leftSide = [] # Min_Heap
        rightSide = [] # Max_Heap
        medianCollection = [] # Returns median or each window
        lazyRemoveVal = defaultdict(int)

        # Step 2: Establish Median Function
        def median() -> float:

            if k & 1: # Bit Operation for efficiency
                return float(-leftSide[0])
            
            return ((-leftSide[0]) + rightSide[0]) / 2.0
        
        # Step 3: Add first k window to two heaps
        for i in range(k):

            # utilize heappushpop to appropriately balance heap
            if len(leftSide) == len(rightSide):
                heapq.heappush(leftSide, -heapq.heappushpop(rightSide, nums[i]))
            
            else:
                heapq.heappush(rightSide, -heapq.heappushpop(leftSide, -nums[i]))
        
        # Add first median val
        medianCollection.append(median())

        # Step 4: Iterate through rest of input arr
        for j in range(k, len(nums)):

            # indirect push to leftSide
            heapq.heappush(leftSide, -heapq.heappushpop(rightSide, nums[j]))

            excl_num = nums[j - k] # val out of k window
            lazyRemoveVal[excl_num] += 1

            # validate where exclu_num could be
            if excl_num > -leftSide[0]:
                heapq.heappush(rightSide, -heapq.heappop(leftSide)) # since we want to prevent heap size difference from exceeding one if excl_num is of rightSide
            
            # Lazy removal
            while leftSide and lazyRemoveVal[-leftSide[0]] > 0:
               lazyRemoveVal[-leftSide[0]] -= 1
               heapq.heappop(leftSide)

            while rightSide and lazyRemoveVal[rightSide[0]] > 0:
               lazyRemoveVal[rightSide[0]] -= 1
               heapq.heappop(rightSide)
            
            # Add respective median vals
            medianCollection.append(median())
    
        return medianCollection
    
# Unit Tests
class TestMedianSlidingWindow(unittest.TestCase):
    def test_median_sliding_window(self):
        solution = Solution()
        
        # # Test case 1: Example from the problem statement
        # nums = [1, 3, -1, -3, 5, 3, 6, 7]
        # k = 3
        # expected = [1.00000, -1.00000, -1.00000, 3.00000, 5.00000, 6.00000]
        # result = solution.medianSlidingWindow(nums, k)
        # for r, e in zip(result, expected):
        #     self.assertAlmostEqual(r, e, delta=1e-5)

        # Test case 2: Another example from the problem statement
        nums = [1, 2, 3, 4, 2, 3, 1, 4, 2]
        k = 3
        expected = [2.00000, 3.00000, 3.00000, 3.00000, 2.00000, 3.00000, 2.00000]
        result = solution.medianSlidingWindow(nums, k)
        for r, e in zip(result, expected):
            self.assertAlmostEqual(r, e, delta=1e-5)

        # # Test case 3: Single element in the array
        # nums = [5]
        # k = 1
        # expected = [5.00000]
        # result = solution.medianSlidingWindow(nums, k)
        # for r, e in zip(result, expected):
        #     self.assertAlmostEqual(r, e, delta=1e-5)

        # # Test case 4: All identical elements
        # nums = [2, 2, 2, 2, 2]
        # k = 2
        # expected = [2.00000, 2.00000, 2.00000, 2.00000]
        # result = solution.medianSlidingWindow(nums, k)
        # for r, e in zip(result, expected):
        #     self.assertAlmostEqual(r, e, delta=1e-5)

        # # Test case 5: Large array, k = 1
        # nums = list(range(1, 1001))
        # k = 1
        # expected = [float(num) for num in nums]
        # result = solution.medianSlidingWindow(nums, k)
        # for r, e in zip(result, expected):
        #     self.assertAlmostEqual(r, e, delta=1e-5)

        # # Test case 6: Large array, k = len(nums)
        # nums = [1, 3, 2, 4]
        # k = 4
        # expected = [2.50000]  # Median of the entire array
        # result = solution.medianSlidingWindow(nums, k)
        # for r, e in zip(result, expected):
        #     self.assertAlmostEqual(r, e, delta=1e-5)

if __name__ == '__main__':
    unittest.main()