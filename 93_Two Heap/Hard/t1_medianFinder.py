from typing import List
import unittest
import heapq

class MedianFinder:

    def __init__(self):
        # Two heaps: max-heap for the lower half and min-heap for the upper half
        self.maxHeap = []  # Simulated max-heap (negative values)
        self.minHeap = []  # Min-heap (positive values)

    def addNum(self, num: int) -> None:
        """
        Add a number to the data structure.
        """
        # Add to maxHeap (lower half), then balance to minHeap
        heapq.heappush(self.maxHeap, -num)

        # Ensure maxHeap's largest (negative) is <= minHeap's smallest
        if self.maxHeap and self.minHeap and -self.maxHeap[0] > self.minHeap[0]:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

        # Balance sizes to make sure the difference is at most 1
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        elif len(self.minHeap) > len(self.maxHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

    def findMedian(self) -> float:
        """
        Return the median of all elements.
        """
        # If odd, return root of the larger heap
        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        # If even, return the average of roots
        return (-self.maxHeap[0] + self.minHeap[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


class TestMedianFinder(unittest.TestCase):
    def test_median_finder(self):
        # Test case 1: Basic functionality
        medianFinder = MedianFinder()
        medianFinder.addNum(1)  # arr = [1]
        self.assertEqual(medianFinder.findMedian(), 1.0)
        medianFinder.addNum(2)  # arr = [1, 2]
        self.assertEqual(medianFinder.findMedian(), 1.5)
        medianFinder.addNum(3)  # arr = [1, 2, 3]
        self.assertEqual(medianFinder.findMedian(), 2.0)
        
    def test_large_inputs(self):
        # Test case 2: Handling larger inputs
        medianFinder = MedianFinder()
        nums = [i for i in range(1, 10001)]  # arr = [1, 2, ..., 10000]
        for num in nums:
            medianFinder.addNum(num)
        self.assertEqual(medianFinder.findMedian(), 5000.5)  # Median of [1..10000]

    def test_negative_and_positive(self):
        # Test case 3: Mix of negative and positive integers
        medianFinder = MedianFinder()
        nums = [-5, -10, -3, 4, 7, 2]
        for num in nums:
            medianFinder.addNum(num)
        self.assertEqual(medianFinder.findMedian(), -0.5)  # Median of sorted [-10, -5, -3, 2, 4, 7]

    def test_single_element(self):
        # Test case 4: Single element in the stream
        medianFinder = MedianFinder()
        medianFinder.addNum(42)
        self.assertEqual(medianFinder.findMedian(), 42.0)

    def test_repeated_elements(self):
        # Test case 5: Repeated elements
        medianFinder = MedianFinder()
        nums = [5, 5, 5, 5, 5]
        for num in nums:
            medianFinder.addNum(num)
        self.assertEqual(medianFinder.findMedian(), 5.0)  # All elements are the same

if __name__ == '__main__':
    unittest.main()