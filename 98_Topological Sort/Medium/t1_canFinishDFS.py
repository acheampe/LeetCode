from typing import List
import unittest

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Determines if all courses can be finished using DFS cycle detection.

        Args:
            numCourses: Total number of courses.
            prerequisites: List of prerequisite pairs [a, b] where b → a.

        Returns:
            True if all courses can be completed, False if there is a cycle.

        Time Complexity: O(V + E) (DFS processes each node and edge once)
        Space Complexity: O(V) (for visited and visiting sets)
        """

        # Create adjacency list (course dependency graph)
        adjList = [[] for _ in range(numCourses)]
        for course, preReq in prerequisites:
            adjList[preReq].append(course)  # Course 'preReq' must be taken before 'course'

        visiting = set()  # Tracks nodes in the current DFS path (detects cycles)
        visited = set()   # Tracks nodes that are confirmed to be cycle-free

        def dfs(node):
            """
            Checks if there's a cycle using DFS.
            
            Args:
                node (int): The current course being checked.
            
            Returns:
                bool: False if a cycle is detected, True otherwise.
            """

            if node in visited:
                return True  # Already confirmed as cycle-free
            if node in visiting:
                return False  # Cycle detected

            visiting.add(node)  # Mark node as visiting (part of current DFS path)

            for neighbor in adjList[node]:
                if not dfs(neighbor):  # If any neighbor leads to a cycle
                    return False

            visiting.remove(node)  # Remove from DFS path after all neighbors are checked
            visited.add(node)  # Mark as safe (cycle-free)

            return True

        # Run DFS for each course
        for i in range(numCourses):
            if i not in visited and not dfs(i):
                return False  # A cycle is detected

        return True  # No cycles found, all courses can be finished
    
    def approachSolution(self):
        """
        If you are familiar with the algorithm to determine if a graph can 
        be sorted topologically, then the most difficult part about this problem
        is realizing that the input given needs to be turned into an adjacentlist
        to represent a graph (I am ashamed to admit how long this took me to realize)

        Once done, we then initiate two set variables, visiting and visited. 
        We then recurse through adjacent graph nodes, if not in visited and or if not 
        recursion (dfs(node) == false). 

        During dfs function, we check to see if node is in visited, if so we return true,
        if not we check if node is in visiting, if it is, we return False.

        If neighter, we update node to add to visiting, recurse through it's neighbor (with if not dfs condition) 
        till we return false, or remove node from visiting to visited, then return true

        TC: O(V + E)
        SC: O(V)
        """

class TestCanFinish(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()  # Assuming the Solution class is correctly implemented

    def test1(self):
        numCourses = 2
        prerequisites = [[1, 0]]
        output = True  # Possible to finish all courses
        self.assertEqual(self.sol.canFinish(numCourses, prerequisites), output)

    def test2(self):
        numCourses = 2
        prerequisites = [[1, 0], [0, 1]]
        output = False  # Cycle exists, impossible to finish
        self.assertEqual(self.sol.canFinish(numCourses, prerequisites), output)

    def test3(self):  # No prerequisites (M                                                                                                                                                                                                                                                                  inimum Constraint)
        numCourses = 3
        prerequisites = []
        output = True  # No dependencies, all courses can be taken
        self.assertEqual(self.sol.canFinish(numCourses, prerequisites), output)

    def test4(self):  # Multiple independent chains
        numCourses = 5
        prerequisites = [[1, 0], [3, 2], [4, 3]]
        output = True  # No cycles, courses can be taken in order
        self.assertEqual(self.sol.canFinish(numCourses, prerequisites), output)

    def test5(self):  # Large cycle
        numCourses = 4
        prerequisites = [[0, 1], [1, 2], [2, 3], [3, 0]]
        output = False  # Cycle exists
        self.assertEqual(self.sol.canFinish(numCourses, prerequisites), output)

    def test6(self):  # Multiple courses, some independent
        numCourses = 6
        prerequisites = [[1, 0], [2, 1], [3, 2], [4, 5]]
        output = True  # No cycle, possible to finish all courses
        self.assertEqual(self.sol.canFinish(numCourses, prerequisites), output)

    def test7(self):  # Large input with no cycles
        numCourses = 10
        prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [9, 8]]
        output = True  # Linear dependency, possible to complete all courses
        self.assertEqual(self.sol.canFinish(numCourses, prerequisites), output)

    def test8(self):  # Large input with a cycle
        numCourses = 10
        prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [9, 8], [0, 9]]
        output = False  # Cycle exists (0 → 9 → 8 → ... → 0)
        self.assertEqual(self.sol.canFinish(numCourses, prerequisites), output)

    def test9(self):  # Disconnected components with a cycle in one part
        numCourses = 6
        prerequisites = [[1, 0], [2, 1], [3, 2], [4, 5], [5, 4]]
        output = False  # Courses 4 and 5 form a cycle
        self.assertEqual(self.sol.canFinish(numCourses, prerequisites), output)

    def test10(self):  # Stress test: Maximum numCourses with no prerequisites
        numCourses = 2000
        prerequisites = []
        output = True  # No dependencies, can finish all courses
        self.assertEqual(self.sol.canFinish(numCourses, prerequisites), output)

    def test11(self): 
        numCourses = 20 
        prerequisites = [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]
        output = False  # Self Loop detection
        self.assertEqual(self.sol.canFinish(numCourses, prerequisites), output)

    def test12(self): 
        numCourses = 5 
        prerequisites = [[1,4],[2,4],[3,1],[3,2]]
        output = True
        self.assertEqual(self.sol.canFinish(numCourses, prerequisites), output)
if __name__ == '__main__':
    unittest.main()