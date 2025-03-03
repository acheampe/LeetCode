import unittest
from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        pass  # Implement your solution here

class TestCountComponents(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test1(self):
        n = 5
        edges = [[0, 1], [1, 2], [3, 4]]
        output = 2
        self.assertEqual(self.sol.countComponents(n, edges), output)

    def test2(self):
        n = 5
        edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
        output = 1
        self.assertEqual(self.sol.countComponents(n, edges), output)

    def test3(self):
        n = 5
        edges = []
        output = 5  # No edges, so each node is its own component
        self.assertEqual(self.sol.countComponents(n, edges), output)

    def test4(self):
        n = 6
        edges = [[0, 1], [2, 3], [4, 5]]
        output = 3
        self.assertEqual(self.sol.countComponents(n, edges), output)

    def test5(self):
        n = 7
        edges = [[0, 1], [1, 2], [3, 4], [5, 6]]
        output = 3
        self.assertEqual(self.sol.countComponents(n, edges), output)

    def test6(self):
        n = 10
        edges = [[0, 1], [1, 2], [3, 4], [5, 6], [7, 8], [8, 9]]
        output = 4
        self.assertEqual(self.sol.countComponents(n, edges), output)

    def test7(self):
        n = 1
        edges = []
        output = 1  # Single node, single component
        self.assertEqual(self.sol.countComponents(n, edges), output)

    def test8(self):
        n = 10
        edges = [[i, i + 1] for i in range(9)]
        output = 1  # Fully connected, single component
        self.assertEqual(self.sol.countComponents(n, edges), output)

if __name__ == '__main__':
    unittest.main()