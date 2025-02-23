from typing import List
import heapq
import unittest
from collections import defaultdict


class Solution: # Failed attempt
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        """
        Return an array of the median in each sliding window of size k.
        Time Complexity: O(n log k) using two heaps.
        Space Complexity: O(k).
        """
        
        # establish variables needed for operation
        min_heap, max_heap = [], [] # min_heap tracks right side (large) and max_heap tracks left side (small value)
        toRemove = defaultdict(int)
        medianCollection = []

        # Set up functions to use to maintain tree balance, remove uneeded val, and to get median
        def balance_heap():
            """Balances both heaps if needed"""
            while len(max_heap) > len(min_heap) + 1: # difference length of 1 at most
                heapq.heappush(min_heap, -heapq.heappop(max_heap))

            while len(min_heap) > len(max_heap): 
                heapq.heappush(max_heap, -heapq.heappop(min_heap))
            
            removeFromHeap() # Ensures removed elements are clearç

        def getMedian():
            """returns median value in current window"""

            if k % 2 != 0:
                return float(-max_heap[0])
            return (((-max_heap[0]) + min_heap[0]) / 2.0)

        def removeFromHeap():
            """Removes value from heap marked for lazy removal"""

            while max_heap and -max_heap[0] in toRemove:
                # remove from heap and recalc dictionary
                toRemove[-max_heap[0]] -= 1
                if toRemove[-max_heap[0]] == 0:
                    del toRemove[-max_heap[0]]
                heapq.heappop(max_heap)

            while min_heap and min_heap[0] in toRemove:
                # remove from heap and recalc dictionary
                toRemove[min_heap[0]] -= 1
                if toRemove[min_heap[0]] == 0:
                    del toRemove[min_heap[0]]  
                heapq.heappop(min_heap)          

        # Initialize first window
        for i in range(k):
            heapq.heappush(max_heap, -nums[i]) # push to max_heap
            balance_heap()
        
        # Add first median val
        medianCollection.append(getMedian())

        for i in range(k, len(nums)):

            # Add out of window vals toRemove
            toRemove[nums[i - k]] += 1

            if nums[i] <= -max_heap[0]:
                heapq.heappush(max_heap, -nums[i]) # push to max_heap
            else:
                heapq.heappush(min_heap, nums[i])
            # remove out of window vals from heap
            removeFromHeap()
            # balance heap
            balance_heap()
            # Add median to result
            medianCollection.append(getMedian())
        
        return medianCollection

# Unit Tests
class TestMedianSlidingWindow(unittest.TestCase):
    def test_median_sliding_window(self):
        solution = Solution()
        
        # Test case 1: Example from the problem statement
        nums = [1, 3, -1, -3, 5, 3, 6, 7]
        k = 3
        expected = [1.00000, -1.00000, -1.00000, 3.00000, 5.00000, 6.00000]
        result = solution.medianSlidingWindow(nums, k)
        for r, e in zip(result, expected):
            self.assertAlmostEqual(r, e, delta=1e-5)

        # # Test case 2: Another example from the problem statement
        # nums = [1, 2, 3, 4, 2, 3, 1, 4, 2]
        # k = 3
        # expected = [2.00000, 3.00000, 3.00000, 3.00000, 2.00000, 3.00000, 2.00000]
        # result = solution.medianSlidingWindow(nums, k)
        # for r, e in zip(result, expected):
        #     self.assertAlmostEqual(r, e, delta=1e-5)

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