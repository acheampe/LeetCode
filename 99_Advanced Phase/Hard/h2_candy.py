import unittest
from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        pass  # Implement your solution here

class TestCandyDistribution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        ratings = [1, 0, 2]
        self.assertEqual(self.solution.candy(ratings), 5)

    def test_example2(self):
        ratings = [1, 2, 2]
        self.assertEqual(self.solution.candy(ratings), 4)

    def test_single_child(self):
        ratings = [5]
        self.assertEqual(self.solution.candy(ratings), 1)

    def test_all_equal(self):
        ratings = [3, 3, 3, 3, 3]
        self.assertEqual(self.solution.candy(ratings), 5)

    def test_strictly_increasing(self):
        ratings = [1, 2, 3, 4, 5]
        self.assertEqual(self.solution.candy(ratings), 15)

    def test_strictly_decreasing(self):
        ratings = [5, 4, 3, 2, 1]
        self.assertEqual(self.solution.candy(ratings), 15)

    def test_valley_case(self):
        ratings = [1, 3, 2, 2, 1]
        self.assertEqual(self.solution.candy(ratings), 7)

if __name__ == "__main__":
    unittest.main()
