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
        
        # Max heap (stores negative values to simulate max heap)
        leftHalf = []
        # Min heap (stores larger half)
        RightHalf = []
        # Dictionary to track numbers to be lazily removed
        toRemove = defaultdict(int)
        # List to store medians
        medianCollection = []

        # add initial window to heap
        for i in range(k):
            if len(leftHalf) == len(RightHalf):
                heapq.heappush(leftHalf, -heapq.heappushpop(RightHalf, nums[i])) # maintain balance with value insertion (more efficent as well - O(log k))
            
            else:
                heapq.heappush(RightHalf, -heapq.heappushpop(leftHalf, -nums[i]))
        
        # add median in initial window
        medianCollection.append(float(-leftHalf[0]) if k & 1 else (RightHalf[0] + (-leftHalf[0])) / 2.0)

        # iterate through rest of num array and push to heap accordingly
        for j in range(k, len(nums)):
            heapq.heappush(leftHalf, -heapq.heappushpop(RightHalf, nums[j])) # maintain balance with added inbound value

            outBoundVal = nums[j - k]
            toRemove[outBoundVal] += 1 # marked for lazy removal

            if outBoundVal > -leftHalf[0]: # to maintain balance
                heapq.heappush(RightHalf, -heapq.heappop(leftHalf))
            
            # Lazy remove process
            while leftHalf and toRemove[-leftHalf[0]] > 0:
                toRemove[-leftHalf[0]] -= 1
                heapq.heappop(leftHalf)

            while RightHalf and toRemove[RightHalf[0]] > 0:
                toRemove[RightHalf[0]] -= 1
                heapq.heappop(RightHalf)

            # add median in initial window
            medianCollection.append(float(-leftHalf[0]) if k & 1 else (RightHalf[0] + (-leftHalf[0])) / 2.0)
    
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

        # Test case 2: Another example from the problem statement
        nums = [1, 2, 3, 4, 2, 3, 1, 4, 2]
        k = 3
        expected = [2.00000, 3.00000, 3.00000, 3.00000, 2.00000, 3.00000, 2.00000]
        result = solution.medianSlidingWindow(nums, k)
        for r, e in zip(result, expected):
            self.assertAlmostEqual(r, e, delta=1e-5)

        # Test case 3: Single element in the array
        nums = [5]
        k = 1
        expected = [5.00000]
        result = solution.medianSlidingWindow(nums, k)
        for r, e in zip(result, expected):
            self.assertAlmostEqual(r, e, delta=1e-5)

        # Test case 4: All identical elements
        nums = [2, 2, 2, 2, 2]
        k = 2
        expected = [2.00000, 2.00000, 2.00000, 2.00000]
        result = solution.medianSlidingWindow(nums, k)
        for r, e in zip(result, expected):
            self.assertAlmostEqual(r, e, delta=1e-5)

        # Test case 5: Large array, k = 1
        nums = list(range(1, 1001))
        k = 1
        expected = [float(num) for num in nums]
        result = solution.medianSlidingWindow(nums, k)
        for r, e in zip(result, expected):
            self.assertAlmostEqual(r, e, delta=1e-5)

        # Test case 6: Large array, k = len(nums)
        nums = [1, 3, 2, 4]
        k = 4
        expected = [2.50000]  # Median of the entire array
        result = solution.medianSlidingWindow(nums, k)
        for r, e in zip(result, expected):
            self.assertAlmostEqual(r, e, delta=1e-5)

if __name__ == '__main__':
    unittest.main()