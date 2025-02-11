from typing import List
from collections import defaultdict
import unittest

from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        Return number of provinces
        """

        n = len(isConnected)
        province = 0
        visited = [False] * n

        def dfs(city):
            """
            explore cities that are connected
            """

            visited[city] = True
            for neighbor in range(n):

                if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                    dfs(neighbor)
            
        
        for i in range(n):
            if not visited[i]:
                dfs(i)
                province += 1

        return province


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