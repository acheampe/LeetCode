from typing import List
from collections import defaultdict
import unittest

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """
        return the max number of subarr length of tree of two types
        """

        # Initial Variables
        fruitsTree = defaultdict(int) # To track count of each fruit in current window
        leftIndex = 0
        maxLengthSubArr = 0

        # Window Expansion Iteration Role
        for rightIndex in range(len(fruits)):
            fruitsTree[fruits[rightIndex]] += 1

            # Window Reduction Iteration Logic
            while len(fruitsTree) > 2:
                fruitsTree[fruits[leftIndex]] -= 1

                # Remove fruit if == 0
                if fruitsTree[fruits[leftIndex]] == 0:
                    del fruitsTree[fruits[leftIndex]]
                
                leftIndex += 1
        
            maxLengthSubArr = max(maxLengthSubArr, rightIndex - leftIndex + 1)

        return maxLengthSubArr

    
      
# sol = Solution()
# print(sol.totalFruit([1,2,1])) # Expected: 3
# print(sol.totalFruit([0,1,2,2])) # Expected: 3
# print(sol.totalFruit([3,3,3,1,2,1,1,2,3,3,4])) # Expected: 5
# print(sol.totalFruit([1,1])) # Expected: 2
# print(sol.totalFruit([3,1,3,2,2])) # Expected: 4

class TestTotalFruit(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
    
    def test_1(self):
        nums = [1, 2, 1]

        expected = 3

        self.assertEqual(self.sol.totalFruit(nums), expected)

    def test_2(self):

        nums = [0,1,2,2]

        expected = 3

        self.assertEqual(self.sol.totalFruit(nums), expected)

    def test_3(self):

        nums = [3,3,3,1,2,1,1,2,3,3,4]

        expected = 5

        self.assertEqual(self.sol.totalFruit(nums), expected)


if __name__ == "__main__":
    unittest.main()