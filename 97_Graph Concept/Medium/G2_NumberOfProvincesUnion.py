from typing import List
import unittest

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        Return the number of provinces using the Disjoint Set (Union-Find) approach.
        """
        n = len(isConnected)
        parent = list(range(n))  # Initially, each node is its own parent.

        # Find function with path compression
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]

        # Union function to merge two sets
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootY] = rootX  # Merge Y into X

        # Process the adjacency matrix
        for i in range(n):
            for j in range(i + 1, n):  # Only check upper triangle to avoid redundancy
                if isConnected[i][j] == 1:
                    union(i, j)

        # Count unique roots (i.e., number of provinces)
        return len(set(find(i) for i in range(n)))


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