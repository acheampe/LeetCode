"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from __future__ import annotations
import unittest

class Solution:
    def cloneGraph(self, node: Node | None) -> Node | None:
        pass
    



class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __eq__(self, other):
        if not other or self.val != other.val:
            return False
        return True  # We'll validate structure in the test case, not here

def graph_to_adj_list(node: 'Node') -> list[list[int]]:
    """Helper function to serialize the graph back to adjacency list."""
    from collections import deque, defaultdict
    visited = set()
    adj = defaultdict(list)
    q = deque([node])
    while q:
        curr = q.popleft()
        if curr.val in visited:
            continue
        visited.add(curr.val)
        for neighbor in curr.neighbors:
            adj[curr.val].append(neighbor.val)
            if neighbor.val not in visited:
                q.append(neighbor)
    return [adj[i] for i in range(1, len(adj) + 1)]

class TestCloneGraph(unittest.TestCase):
    def build_graph(self, adj_list: list[list[int]]) -> Node | None:
        """Builds a graph from an adjacency list representation."""
        if not adj_list:
            return None
        nodes = {}
        for i in range(1, len(adj_list) + 1):
            nodes[i] = Node(i)
        for i, neighbors in enumerate(adj_list, start=1):
            nodes[i].neighbors = [nodes[n] for n in neighbors]
        return nodes[1]

    def test_clone_graph_4_nodes(self):
        adj_list = [[2, 4], [1, 3], [2, 4], [1, 3]]
        original = self.build_graph(adj_list)
        cloned = Solution().cloneGraph(original)
        self.assertEqual(graph_to_adj_list(cloned), adj_list)

    def test_clone_graph_single_node_no_neighbors(self):
        adj_list = [[]]
        original = self.build_graph(adj_list)
        cloned = Solution().cloneGraph(original)
        self.assertEqual(graph_to_adj_list(cloned), adj_list)

    def test_clone_graph_empty(self):
        adj_list = []
        original = self.build_graph(adj_list)
        cloned = Solution().cloneGraph(original)
        self.assertIsNone(cloned)

if __name__ == "__main__":
    unittest.main()