import unittest

class Solution:
    def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:
        pass


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