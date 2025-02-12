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

    def solutionApproach(self):
        """
        Approaching this problem using DFS takes a bit of ingenuity...at least
        for me. 

        The first thing is to establish variables/memory needed for dfs operation.

        This involves, a counter for province, an array containing False
        (to mark visited) of length of isConnected array.

        from here we create a for loop for isConnected, and if current city is
        not visited, we call dfs function, to mark current city as visited, then
        explore it's adjacent neighbors to if it is visited or not. 

        if not visited, then we call dfs to explore that city and it's connections

        and whenever we exit dfs, we count exploration as a province, since dfs 
        is integrated to explore one connected province at a time. 

        Future use: This is a great approach to have when needing to explore all
        connected paths at a time to solve a problem.

        Space Complexity: O (n) complexity worse case. 
        Time Complexity: O(n^2) due to matrix array
        """

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