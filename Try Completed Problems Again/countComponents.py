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

        TC: O (V + E) - path compression
        SC: O (V) - for storing parents
        """
        # establish parent in array
        parent = [i for i in range(n)]

        # Find parent of city
        def find(city):
            
            if parent[city] != city:
                parent[city] = find(parent[city])
            return parent[city]
        
        # Unit city into one province
        def Union(city1, city2):

            province1, province2 = find(city1), find(city2)

            if province1 != province2:
                parent[province2] = province1 # path compression
        
        for edge in edges:
            Union(edge[0], edge[1]) # unite if diff parents
        
        addProvinces = set()
        for i in range(n):
            addProvinces.add(find(i))
        
        return len(addProvinces)

            

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