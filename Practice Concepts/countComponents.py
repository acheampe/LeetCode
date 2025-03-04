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

        parent = [i for i in range(n)]

        # find parent
        def find(city):
            """returns parent city"""

            if parent[city] != city:
                parent[city] = find(parent[city])
            
            return parent[city]

        def union(city1 , city2):
            """unites cities with edges"""

            root1 = find(city1)
            root2 = find(city2)

            if root1 != root2:
                parent[root2] = root1 # path compression
        
        for edge in edges:
            union(edge[0], edge[1])
        
        # Add distinguished provinces
        provinces =set()

        for i in range(n):
            provinces.add(find(i))
        
        return len(provinces)

    def approachSolution(self):
        """
        This problem requires finding the number of **connected components** in an **undirected graph**. 
        The **Union-Find (Disjoint Set Union - DSU)** data structure is an optimal approach to efficiently 
        group connected nodes while leveraging **path compression** for near O(1) operations.

        🚀 **Steps to Solve the Problem Efficiently:**

        1️⃣ **Initialize the Parent Array**  
        - Create an array `parent` where each node is initially its own parent.

        2️⃣ **Define Find and Union Functions**  
        - **Find:** Recursively finds the root of a node, applying **path compression** 
            (updates parent pointers to the root for efficiency).
        - **Union:** Connects two nodes by setting the parent of one node's root to the other.

        3️⃣ **Process All Edges**  
        - Iterate through `edges` and apply `union(edge[0], edge[1])` to merge connected nodes.

        4️⃣ **Count Distinct Components**  
        - Traverse all nodes and apply `find(i)` to determine their root parent.
        - Store unique root parents in a `set`, representing distinct connected components.

        5️⃣ **Return the Number of Unique Components**  
        - The number of unique roots in the `set` is the number of connected components.

        🔹 **Key Learnings:**
        - **Union-Find with path compression** improves performance close to **O(1)**.
        - **Using a `set` to count unique roots** is an efficient way to determine the number of components.
        - **Path compression reduces tree height**, making `find()` operations more efficient.

        ⏳ **Time Complexity:** O(V + E) (amortized O(1) due to path compression)  
        🏗 **Space Complexity:** O(V) (for parent array storage)
        """


# DFS Approach
# class Solution:
#     def countComponents(self, n: int, edges: List[List[int]]) -> int:
#         """
#         Return the number of connected components in an undirected graph using DFS.

#         Args:
#             n (int): Number of nodes.
#             edges (List[List[int]]): List of undirected edges.

#         Returns:
#             int: Number of connected components.

#         Time Complexity: O(V + E) (DFS traversal)
#         Space Complexity: O(V + E) (Adjacency list + visited set)
#         """

#         # Step 1: Build adjacency list
#         graph = {i: [] for i in range(n)}
#         for u, v in edges:
#             graph[u].append(v)
#             graph[v].append(u)  # Undirected graph

#         visited = set()  # Track visited nodes
#         components = 0    # Count of connected components

#         # Step 2: DFS function to traverse the component
#         def dfs(node):
#             """Performs DFS to mark all reachable nodes from 'node' as visited"""
#             stack = [node]
#             while stack:
#                 curr = stack.pop()
#                 for neighbor in graph[curr]:
#                     if neighbor not in visited:
#                         visited.add(neighbor)
#                         stack.append(neighbor)

#         # Step 3: Iterate through all nodes
#         for i in range(n):
#             if i not in visited:
#                 components += 1  # New component found
#                 visited.add(i)    # Mark the node as visited
#                 dfs(i)            # Perform DFS from this node
        
#         return components

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