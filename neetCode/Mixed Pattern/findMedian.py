import heapq
import unittest

class MedianFinder:

    def __init__(self):
        self.leftSideHeap = [] # maxHeap
        self.rightSideHeap = [] # minHeap

    def addNum(self, num: int) -> None:
        if len(self.leftSideHeap) == len(self.rightSideHeap):
            heapq.heappush(self.leftSideHeap, -heapq.heappushpop(self.rightSideHeap, num))
        else:
            heapq.heappush(self.rightSideHeap, -heapq.heappushpop(self.leftSideHeap, -num))            
        

    def findMedian(self) -> float:
        if len(self.leftSideHeap) > len(self.rightSideHeap):
            return -float(self.leftSideHeap[0])
        return ((-self.leftSideHeap[0]) + self.rightSideHeap[0])/ 2.0

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

    def test_input_output_sequence(self):
        mf = MedianFinder()
        operations = ["addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian"]
        arguments = [[-1], [], [-2], [], [-3], [], [-4], [], [-5], []]
        expected = [None, -1.00000, None, -1.50000, None, -2.00000, None, -2.50000, None, -3.00000]

        result = [None]  # First call is the constructor

        for op, arg in zip(operations, arguments):
            if op == "addNum":
                result.append(mf.addNum(*arg))
            elif op == "findMedian":
                result.append(mf.findMedian())

        self.assertEqual(result, [None] + expected)

if __name__ == '__main__':
    unittest.main()