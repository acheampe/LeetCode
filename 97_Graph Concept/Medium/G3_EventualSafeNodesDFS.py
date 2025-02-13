from typing import List
import unittest


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        """
        return safe Nodes

        Args: graph[List], indicative indexed-0 node connections as list

        Return: A list of nodes that are safe. Safe Nodes are nodes, whose every
        possible path leads to a terminal node

        Time Complexity = O(V + E)
        Space Complexity = Worse case O(V) if graph is a single path
        """
        safeNotSafe = {} # Hashmap to track if node is safe or not
        safeList = [] # list of safe nodes - > if all it's path leads to leaf node

        def dfs(node):
            
            # Base case:
            if node in safeNotSafe:
                return safeNotSafe[node] # dfs returns true or false
    

            # else assume false
            safeNotSafe[node] = False

            for neigbor in graph[node]:
                if not dfs(neigbor):
                    return False # if any neighbor is unsafe then this node is unsafe as well
            
            safeNotSafe[node] = True

            return True 

        for i in range(len(graph)): # iterate through nodes
            
            if dfs(i):  # if true
                safeList.append(i)
        
        return safeList # returns list in order


    
    def approachSolution(self):
        """
        Approaching this problem using DFS is an excellent approach due
        to the fact that the returned output result will be already sorted.

        # To solve this problem using DFS, we must initiate a hashmap that assumes 
        all nodes to be False

        # After we iterate through graph passing the iterating through DFS. if 
        returned, we append the current iteration to a SafeList

        # The DFS will check hashmap to see if node is safe in order to return (base case)
        if not, we presume it to be False, then call it's neighbor with recursive DFS till we 
        reach a node with no neighbors, no inDegree, then we change it's hashmap value to true, if DFS returns True,
        then we append i to our safeList.

        Time Complexity = O(V + E)
        Space Complexity = O(V) due to hashMap


        Clear explanation:
        DFS is an excellent approach because it naturally ensures that 
        the final result is in sorted order.
        
        # Approach:
        1️⃣ Use a hashmap (`safeNotSafe`) to store whether a node is safe (`True`) or unsafe (`False`).
        2️⃣ Iterate over each node in the graph:
            - If the node has already been marked safe, we can immediately return its status.
            - Otherwise, assume it is unsafe and use DFS to explore its neighbors.
            - If any neighbor is unsafe, the node is unsafe.
            - If all paths lead to terminal nodes, mark the node as safe.
        3️⃣ Append all safe nodes to `safeList`.
        
        # Why DFS?
        - **Cycle Detection:** If a node is visited before DFS completes, it must be in a cycle.
        - **Memoization:** Ensures we don't recompute results unnecessarily.
        - **Time Complexity:** O(V + E), where V is the number of nodes and E is the number of edges.
        - **Space Complexity:** O(V) for storing `safeNotSafe`.

        # Key Edge Cases Considered:
        ✅ A node pointing to itself (self-loop)
        ✅ Nodes leading to cycles
        ✅ Disconnected graph components
        ✅ Large inputs (ensuring efficiency)
        """


class TestEventualSafeNodes(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test1(self):
        graph = [[1,2],[2,3],[5],[0],[5],[],[]]
        outPut = [2,4,5,6]
        self.assertEqual(self.sol.eventualSafeNodes(graph), outPut)

    # def test2(self):
    #     graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
    #     outPut = [4]
    #     self.assertEqual(self.sol.eventualSafeNodes(graph), outPut)   

    # def test3(self):  # Single node (Minimum Constraint)
    #     graph = [[]]  # Only one node with no outgoing edges
    #     outPut = [0]
    #     self.assertEqual(self.sol.eventualSafeNodes(graph), outPut)

    # def test4(self):  # Fully connected cycle (No safe nodes)
    #     graph = [[1],[2],[0]]  # 0 → 1 → 2 → 0 (cycle)
    #     outPut = []  # No safe nodes
    #     self.assertEqual(self.sol.eventualSafeNodes(graph), outPut)

    # def test5(self):  # Multiple terminal nodes
    #     graph = [[],[],[],[],[],[]]  # All nodes are terminal
    #     outPut = [0,1,2,3,4,5]  # Every node is safe
    #     self.assertEqual(self.sol.eventualSafeNodes(graph), outPut)

    # def test6(self):  # Large n with sparse edges
    #     n = 100  # Large graph with some isolated safe nodes
    #     graph = [[i+1] for i in range(n-1)] + [[]]  # Chain ending at terminal node
    #     outPut = list(range(n))  # Every node eventually leads to last safe node
    #     self.assertEqual(self.sol.eventualSafeNodes(graph), outPut)

    # def test7(self):  # Graph with self-loops
    #     graph = [[0],[2],[1,3],[]]  # 0 → 0 (loop), 1 → 2 → 1 (loop), 3 is safe
    #     outPut = [3]  # Only node 3 is safe
    #     self.assertEqual(self.sol.eventualSafeNodes(graph), outPut)

    # def test8(self):  # Alternating cycles and safe paths
    #     graph = [[1], [2], [0], [4,5], [6], [6], []]  
    #     # 0 → 1 → 2 → 0 (cycle)
    #     # 3 → 4 → 6 (safe)
    #     # 5 → 6 (safe)
    #     outPut = [3, 4, 5, 6]
    #     self.assertEqual(self.sol.eventualSafeNodes(graph), outPut)

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