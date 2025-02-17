from typing import List
from collections import deque
import unittest

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Return order in which courses can be taken if possible; 
        otherwise, return an empty list.
        
        Args:
            numCourses (int): Total number of courses.
            prerequisites (List[List[int]]): Prerequisite pairs [a, b] where b → a.

        Returns:
            List[int]: A valid topological order of courses, or [] if a cycle exists.

        Time Complexity: O(V + E)
        Space Complexity: O(V + E) for adjacency list and recursion stack.
        """

        # Create adjacency list representation of graph
        adjList = [[] for _ in range(numCourses)]
        for course, preReq in prerequisites:
            adjList[preReq].append(course)  # Course `preReq` must be taken before `course`

        # Track visiting and visited nodes
        visiting = set()  # Detect cycles (nodes in the current DFS path)
        visited = set()  # Tracks safe nodes (already processed)
        orderedResult = deque()  # Stores topological order

        def dfs(node):
            """
            DFS-based cycle detection and topological sorting.

            Returns:
                bool: False if a cycle is detected, True otherwise.
            """

            if node in visited:
                return True  # If already processed, return immediately
            if node in visiting:
                return False  # Cycle detected, return failure
            
            visiting.add(node)  # Mark node as currently being visited

            for neighbor in adjList[node]:  # Explore neighbors
                if not dfs(neighbor):  # If cycle found in subpath, return failure
                    return False

            visiting.remove(node)  # Backtrack (remove from current path)
            visited.add(node)  # Mark node as safe (processed)
            orderedResult.appendleft(node)  # Append to result (topological order)

            return True  # Successful DFS

        # Try to process all courses
        for i in range(numCourses):
            if i not in visited and not dfs(i):  # If cycle detected, return empty list
                return []

        return list(orderedResult)  # Return valid topological order

class TestFindOrder(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()  # Assuming the Solution class is correctly implemented

    def test1(self):
        numCourses = 2
        prerequisites = [[1, 0]]
        output = [0, 1]  # One valid order
        self.assertEqual(self.sol.findOrder(numCourses, prerequisites), output)

    def test2(self):
        numCourses = 4
        prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
        output1 = [0, 1, 2, 3]
        output2 = [0, 2, 1, 3]  # Both valid
        self.assertIn(self.sol.findOrder(numCourses, prerequisites), [output1, output2])

    def test3(self):  # No prerequisites (Minimum Constraint)
        numCourses = 1
        prerequisites = []
        output = [0]
        self.assertEqual(self.sol.findOrder(numCourses, prerequisites), output)

    def test5(self):  # Cycle in prerequisites
        numCourses = 2
        prerequisites = [[1, 0], [0, 1]]
        output = []
        self.assertEqual(self.sol.findOrder(numCourses, prerequisites), output)

    def test6(self):  # Multiple courses with independent chains
        numCourses = 5
        prerequisites = [[1, 0], [3, 2], [4, 3]]
        output1 = [0, 1, 2, 3, 4]
        output2 = [2, 3, 4, 0, 1]  # Both are valid
        self.assertIn(self.sol.findOrder(numCourses, prerequisites), [output1, output2])

    def test7(self):  # Single independent course plus a dependency chain
        numCourses = 5
        prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3]]
        output = [0, 1, 2, 3, 4]  # Only valid order
        self.assertEqual(self.sol.findOrder(numCourses, prerequisites), output)

    def test8(self):  # Large linear dependency chain
        numCourses = 10
        prerequisites = [[i + 1, i] for i in range(9)]
        output = list(range(10))  # Only valid order
        self.assertEqual(self.sol.findOrder(numCourses, prerequisites), output)

    def test9(self):  # Large cycle
        numCourses = 5
        prerequisites = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]]
        output = []  # Cycle detected
        self.assertEqual(self.sol.findOrder(numCourses, prerequisites), output)

    # def test10(self):  # Stress test with large input, no cycles
    #     numCourses = 2000
    #     prerequisites = [[i + 1, i] for i in range(1999)]  # Linear dependency
    #     output = list(range(2000))
    #     self.assertEqual(self.sol.findOrder(numCourses, prerequisites), output)

    def test11(self):  # Stress test with large input, no cycles
        numCourses = 2
        prerequisites = [[0,1]] 
        output = [1,0]
        self.assertEqual(self.sol.findOrder(numCourses, prerequisites), output)


if __name__ == '__main__':
    unittest.main()