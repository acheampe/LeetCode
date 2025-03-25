import unittest
import heapq

class MedianFinder:
    """
    Time Complexity = O(log n)
    Space Complexity = O(n)
    """

    def __init__(self):
        self.leftSide = [] # maxHeap
        self.rightSide = [] # minHeap
        

    def addNum(self, num: int) -> None:
        
        if len(self.leftSide) <= len(self.rightSide):
            heapq.heappush(self.leftSide, -heapq.heappushpop(self.rightSide, num)) # O (log n)
        
        else:
            heapq.heappush(self.rightSide, -heapq.heappushpop(self.leftSide, -num)) # O (log n)

    def findMedian(self) -> float:
        
        if len(self.leftSide) > len(self.rightSide):
            return -float(self.leftSide[0])
        
        return ((-self.leftSide[0]) + self.rightSide[0]) / 2.0


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