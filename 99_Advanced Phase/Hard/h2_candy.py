import unittest
from typing import List
from collections import defaultdict

class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
        return total sum of candies given out

        Arg: List[int]

        return: int
        """

        trackTally = [1 for _ in range(len(ratings))]

        for i in range(len(ratings) - 1):

            if ratings[i] > ratings[i + 1]:
                trackTally[i] += 1
            
            elif ratings[i + 1] > ratings[i]:
                trackTally[i + 1] += trackTally[i]
        
        return sum(trackTally) # O(n)


class TestCandyDistribution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    # def test_example1(self):
    #     ratings = [1, 0, 2]
    #     self.assertEqual(self.solution.candy(ratings), 5)

    # def test_example2(self):
    #     ratings = [1, 2, 2]
    #     self.assertEqual(self.solution.candy(ratings), 4)

    # def test_single_child(self):
    #     ratings = [5]
    #     self.assertEqual(self.solution.candy(ratings), 1)

    # def test_all_equal(self):
    #     ratings = [3, 3, 3, 3, 3]
    #     self.assertEqual(self.solution.candy(ratings), 5)

    # def test_strictly_increasing(self):
    #     ratings = [1, 2, 3, 4, 5]
    #     self.assertEqual(self.solution.candy(ratings), 15)

    # def test_strictly_decreasing(self):
    #     ratings = [5, 4, 3, 2, 1]
    #     self.assertEqual(self.solution.candy(ratings), 15)

    def test_valley_case(self):
        ratings = [1, 3, 2, 2, 1]
        self.assertEqual(self.solution.candy(ratings), 7)

if __name__ == "__main__":
    unittest.main()
