from typing import List
import heapq
from collections import defaultdict
import unittest


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        """
        Return an array of the median in each sliding window of size k.
        Time Complexity: O(n log k) using two heaps.
        Space Complexity: O(k).
        """

        # Min heap (right half) stores larger numbers
        minHeap = []
        # Max heap (left half) stores smaller numbers (inverted)
        maxHeap = []
        # Dictionary to track elements to remove lazily
        removalMap = defaultdict(int)
        result = []

        def balance_heaps():
            """Ensures maxHeap has at most one more element than minHeap."""
            while len(maxHeap) > len(minHeap) + 1:
                heapq.heappush(minHeap, -heapq.heappop(maxHeap))
            while len(minHeap) > len(maxHeap):
                heapq.heappush(maxHeap, -heapq.heappop(minHeap))

        def remove_invalid():
            """Removes elements from the top of the heaps that are marked for removal."""
            while maxHeap and removalMap[-maxHeap[0]]:
                removalMap[-maxHeap[0]] -= 1
                heapq.heappop(maxHeap)
            while minHeap and removalMap[minHeap[0]]:
                removalMap[minHeap[0]] -= 1
                heapq.heappop(minHeap)

        def get_median():
            """Returns the median based on the current window."""
            if k % 2 == 1:
                return float(-maxHeap[0])
            return (-maxHeap[0] + minHeap[0]) / 2.0

        # Build initial window
        for i in range(k):
            heapq.heappush(maxHeap, -nums[i])
        for _ in range(k // 2):
            heapq.heappush(minHeap, -heapq.heappop(maxHeap))

        # First median
        result.append(get_median())

        # Sliding window processing
        for i in range(k, len(nums)):
            out_num = nums[i - k]  # Number to be removed
            in_num = nums[i]  # New number to be inserted

            # Mark out_num for removal
            removalMap[out_num] += 1

            # Insert new number into the correct heap
            if in_num <= -maxHeap[0]:  # Correctly compare with maxHeap top
                heapq.heappush(maxHeap, -in_num)
            else:
                heapq.heappush(minHeap, in_num)

            # Balance heaps first
            balance_heaps()
            
            # Remove outdated elements **before** computing median
            remove_invalid() 

            # Append median
            result.append(get_median())

        return result

# Unit Tests
class TestMedianSlidingWindow(unittest.TestCase):
    def test_median_sliding_window(self):
        solution = Solution()

        # Test case 1
        nums = [1, 3, -1, -3, 5, 3, 6, 7]
        k = 3
        expected = [1.00000, -1.00000, -1.00000, 3.00000, 5.00000, 6.00000]
        result = solution.medianSlidingWindow(nums, k)
        for r, e in zip(result, expected):
            self.assertAlmostEqual(r, e, delta=1e-5)

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