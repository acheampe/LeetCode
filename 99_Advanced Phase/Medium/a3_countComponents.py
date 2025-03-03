from typing import List
import unittest

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        Return the number of connected components in an undirected graph.

        Args:
            n (int): Number of nodes.
            edges (List[List[int]]): List of undirected edges.

        Returns:
            int: Number of connected components.

        Time Complexity: O(V + E) (near O(1) with path compression)
        Space Complexity: O(V) (for parent array)
        """

        # Initialize parent array where each node is its own parent
        parent = [i for i in range(n)]

        # Find function with path compression
        def find(city):
            if parent[city] != city:
                parent[city] = find(parent[city])  # Path compression
            return parent[city]

        # Union function to merge sets
        def union(city1, city2):
            root1 = find(city1)
            root2 = find(city2)

            if root1 != root2:
                parent[root2] = root1  # Merge the sets

        # Process all edges
        for city1, city2 in edges:
            union(city1, city2)

        # Count unique root nodes (distinct components)
        return len(set(find(i) for i in range(n)))
            

class TestCountComponents(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test1(self):
        n = 5
        edges = [[0, 1], [1, 2], [3, 4]]
        output = 2
        self.assertEqual(self.sol.countComponents(n, edges), output)

    # def test2(self):
    #     n = 5
    #     edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
    #     output = 1
    #     self.assertEqual(self.sol.countComponents(n, edges), output)

    # def test3(self):
    #     n = 5
    #     edges = []
    #     output = 5  # No edges, so each node is its own component
    #     self.assertEqual(self.sol.countComponents(n, edges), output)

    # def test4(self):
    #     n = 6
    #     edges = [[0, 1], [2, 3], [4, 5]]
    #     output = 3
    #     self.assertEqual(self.sol.countComponents(n, edges), output)

    # def test5(self):
    #     n = 7
    #     edges = [[0, 1], [1, 2], [3, 4], [5, 6]]
    #     output = 3
    #     self.assertEqual(self.sol.countComponents(n, edges), output)

    # def test6(self):
    #     n = 10
    #     edges = [[0, 1], [1, 2], [3, 4], [5, 6], [7, 8], [8, 9]]
    #     output = 4
    #     self.assertEqual(self.sol.countComponents(n, edges), output)

    # def test7(self):
    #     n = 1
    #     edges = []
    #     output = 1  # Single node, single component
    #     self.assertEqual(self.sol.countComponents(n, edges), output)

    # def test8(self):
    #     n = 10
    #     edges = [[i, i + 1] for i in range(9)]
    #     output = 1  # Fully connected, single component
    #     self.assertEqual(self.sol.countComponents(n, edges), output)

if __name__ == '__main__':
    unittest.main()