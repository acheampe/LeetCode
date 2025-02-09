from typing import List
from collections import defaultdict
import unittest

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        Return number of provinces

        Arg: List of List[int]

        Return: Int -> indicates number of provinces
        """
        
        # Establish variables needed for operation
        countProvince = 0 # increment/decrement province when conditions are met
        adjMatrix = defaultdict(int)
        visitedSet = set()

        # Iterate through isConnected
        for i in range(len(isConnected)): # O(n) operation
            for j in range(len(isConnected[i])): # O(n) operation
                
                if isConnected[i][j] == 1:
                    
                    # Track provinces
                    if i == j:
                        adjMatrix[tuple(sorted((i,j)))] += 1
                        countProvince += 1
                        visitedSet.add((tuple(sorted((i,j)))))
                    
                    elif tuple(sorted((i,i))) not in visitedSet and tuple(sorted((i,j))) not in visitedSet and \
                        adjMatrix[tuple(sorted((i,j)))] == 0:
                        countProvince += 1 # to count them as one province
                        adjMatrix[tuple(sorted((i,i)))] += 1
                        visitedSet.add((tuple(sorted((i,j)))))
        
        return countProvince
        


class TestFindCircleNum(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test1(self):
        isConnected = [[1,1,0],[1,1,0],[0,0,1]]
        outPut = 2
        self.assertEqual(self.sol.findCircleNum(isConnected), outPut)

    # def test2(self):
    #     isConnected = [[1,0,0],[0,1,0],[0,0,1]]
    #     outPut = 3
    #     self.assertEqual(self.sol.findCircleNum(isConnected), outPut)

    # def test3(self):  # Single city (Minimum Constraint)
    #     isConnected = [[1]]
    #     outPut = 1
    #     self.assertEqual(self.sol.findCircleNum(isConnected), outPut)

    # def test4(self):  # Fully connected cities (One province)
    #     isConnected = [[1,1,1],[1,1,1],[1,1,1]]
    #     outPut = 1
    #     self.assertEqual(self.sol.findCircleNum(isConnected), outPut)

    # def test5(self):  # Large n with a single province (Fully connected)
    #     isConnected = [[1]*10 for _ in range(10)]
    #     outPut = 1
    #     self.assertEqual(self.sol.findCircleNum(isConnected), outPut)

    # def test6(self):  # Large n with no connections (Each city is its own province)
    #     isConnected = [[1 if i == j else 0 for j in range(10)] for i in range(10)]
    #     outPut = 10
    #     self.assertEqual(self.sol.findCircleNum(isConnected), outPut)

    # def test7(self):  # Multiple small provinces
    #     isConnected = [
    #         [1,1,0,0,0],
    #         [1,1,0,0,0],
    #         [0,0,1,1,0],
    #         [0,0,1,1,0],
    #         [0,0,0,0,1]
    #     ]
    #     outPut = 3
    #     self.assertEqual(self.sol.findCircleNum(isConnected), outPut)

    # def test8(self):  # Complex province structure
    #     isConnected = [
    #         [1,1,0,0,0,0],
    #         [1,1,1,0,0,0],
    #         [0,1,1,0,0,0],
    #         [0,0,0,1,1,0],
    #         [0,0,0,1,1,1],
    #         [0,0,0,0,1,1]
    #     ]
    #     outPut = 2
    #     self.assertEqual(self.sol.findCircleNum(isConnected), outPut)

    # def test9(self):  # Alternating connections forming separate provinces
    #     isConnected = [
    #         [1,0,1,0,1],
    #         [0,1,0,1,0],
    #         [1,0,1,0,1],
    #         [0,1,0,1,0],
    #         [1,0,1,0,1]
    #     ]
    #     outPut = 3
    #     self.assertEqual(self.sol.findCircleNum(isConnected), outPut)

    # def test10(self):  # Stress test (near upper bound n = 50)
    #     import random
    #     n = 50
    #     isConnected = [[1 if i == j or random.random() < 0.05 else 0 for j in range(n)] for i in range(n)]
    #     # Output is unknown but ensures performance on large inputs.
    #     self.assertIsInstance(self.sol.findCircleNum(isConnected), int)

if __name__ == '__main__':
    unittest.main()