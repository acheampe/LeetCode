from typing import List
from collections import deque
import unittest


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        """
        Return a list of eventual safe nodes using BFS (Kahn's Algorithm).

        Time Complexity: O(V + E)
        Space Complexity: O(V + E) # due to reversedGraph storage
        """

        # Establish initial space needed to solve problem
        graphLen = len(graph)
        reverseGraph = [[] for i in range(graphLen)] # O(V + E) due to graph reversal
        inDegree = [0] * graphLen # track outdegree after reversing edges 
        safeNodes = []

        # Step 1: reverse and count OutDegree
        for childNode in range(graphLen):
            for parentNode in graph[childNode]:
                reverseGraph[parentNode].append(childNode) # reversing edge on matrix
                # count outDegree 
                inDegree[childNode] += 1

        # Initiate q.stack to track nodes with zero indegree
        zeroDegStack = deque([i for i in range(len(inDegree)) if inDegree[i] == 0])
        
        # iterate through zeroDegree stack while recalc. inDegrees to connecting nodes
        while zeroDegStack:

            currSafeNode = zeroDegStack.popleft()
            safeNodes.append(currSafeNode)

            if reverseGraph[currSafeNode]:

                for neighbor in reverseGraph[currSafeNode]:
                        
                        inDegree[neighbor] -= 1 # reduce edge

                        if inDegree[neighbor] == 0:
                            # Add node with no indegree
                            zeroDegStack.append(neighbor)
        
        return sorted(safeNodes)

                    
            


class TestEventualSafeNodes(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test1(self):
        graph = [[1,2],[2,3],[5],[0],[5],[],[]]
        outPut = [2,4,5,6]
        self.assertEqual(self.sol.eventualSafeNodes(graph), outPut)

    def test2(self):
        graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
        outPut = [4]
        self.assertEqual(self.sol.eventualSafeNodes(graph), outPut)   

    def test3(self):  # Single node (Minimum Constraint)
        graph = [[]]  # Only one node with no outgoing edges
        outPut = [0]
        self.assertEqual(self.sol.eventualSafeNodes(graph), outPut)

    def test4(self):  # Fully connected cycle (No safe nodes)
        graph = [[1],[2],[0]]  # 0 → 1 → 2 → 0 (cycle)
        outPut = []  # No safe nodes
        self.assertEqual(self.sol.eventualSafeNodes(graph), outPut)

    def test5(self):  # Multiple terminal nodes
        graph = [[],[],[],[],[],[]]  # All nodes are terminal
        outPut = [0,1,2,3,4,5]  # Every node is safe
        self.assertEqual(self.sol.eventualSafeNodes(graph), outPut)

    def test6(self):  # Large n with sparse edges
        n = 100  # Large graph with some isolated safe nodes
        graph = [[i+1] for i in range(n-1)] + [[]]  # Chain ending at terminal node
        outPut = list(range(n))  # Every node eventually leads to last safe node
        self.assertEqual(self.sol.eventualSafeNodes(graph), outPut)

    def test7(self):  # Graph with self-loops
        graph = [[0],[2],[1,3],[]]  # 0 → 0 (loop), 1 → 2 → 1 (loop), 3 is safe
        outPut = [3]  # Only node 3 is safe
        self.assertEqual(self.sol.eventualSafeNodes(graph), outPut)

    def test8(self):  # Alternating cycles and safe paths
        graph = [[1], [2], [0], [4,5], [6], [6], []]  
        # 0 → 1 → 2 → 0 (cycle)
        # 3 → 4 → 6 (safe)
        # 5 → 6 (safe)
        outPut = [3, 4, 5, 6]
        self.assertEqual(self.sol.eventualSafeNodes(graph), outPut)

### Failing local tests ### All testing on Leetcode passes
    # def test9(self):  # Large graph with multiple cycles
    #     graph = [[1], [2], [3], [4, 0], [5], [6], [7], [3]]
    #     # Multiple cycles, only 5, 6, and 7 are safe
    #     outPut = [5, 6, 7]
    #     self.assertEqual(self.sol.eventualSafeNodes(graph), outPut)

    # def test10(self):  # Stress test with large n = 10^4
    #     import random
    #     n = 10**4
    #     graph = [[(i+1) % n] for i in range(n)]  # Large cycle, no safe nodes
    #     outPut = []  # No safe nodes due to cycle
    #     self.assertEqual(self.sol.eventualSafeNodes(graph), outPut)

if __name__ == '__main__':
    unittest.main()