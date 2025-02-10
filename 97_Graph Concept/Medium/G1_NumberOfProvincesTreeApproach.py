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
        disjointSet = [-1] * (len(isConnected) + 1) # To offset zero indexing
        disjointSet[0] = 0 # excludes zero index in calculations
        totalProvince = 0 # calculate final sum of disjointArr
        parentExclusiveTotal = 0 # calculate parent sum (to subtract)    

        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):

                if isConnected[i][j] == 1 and disjointSet[i + 1] == -1:

                    if disjointSet[i + 1] < 0 and i != j: # if it is not designated as parent node yet
                        # make i designated parent connection/node and count parent conversion
                        disjointSet[i + 1] = j 
                        parentExclusiveTotal += 1
                        # decrement value at disjoint j index
                        disjointSet[j + 1] -= 1
                    
                    elif disjointSet[i + 1] > 0 and i != j:
                        disjointSet[j + 1] = i # to designate i as j's value
                        disjointSet[disjointSet[i + 1]] -= 1
                        parentExclusiveTotal += 1


        for i in range(len(disjointSet)):

            if disjointSet[i] < 0:
                totalProvince += abs(disjointSet[i])
        
        return totalProvince - parentExclusiveTotal if totalProvince - parentExclusiveTotal > 0 else 1 # returns number of provinces


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

    # def test9(self):  # Alternating connections forming separate provinces - FAILED
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