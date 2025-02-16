from typing import List
from collections import deque
import unittest

from typing import List
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Determines if all courses can be finished using Kahn's Algorithm (BFS topological sorting).

        Args:
            numCourses: Total number of courses.
            prerequisites: List of prerequisite pairs [a, b] where b → a.

        Returns:
            True if all courses can be completed, False if there is a cycle.

        Time Complexity: O(V + E) (Processing each node and edge once)
        Space Complexity: O(V + E) (For adjacency list and in-degree tracking)
        """

        # Step 1: Create adjacency list & track in-degrees
        adjList = [[] for _ in range(numCourses)]
        inDegree = [0] * numCourses

        for course, preReq in prerequisites:
            adjList[preReq].append(course)  # Normal direction (preReq → course)
            inDegree[course] += 1  # Count in-degrees for courses

        # Step 2: Initialize queue with zero in-degree courses (starting points)
        zeroDegreeQueue = deque([i for i in range(numCourses) if inDegree[i] == 0])

        # Step 3: Process courses with zero in-degree
        count = 0  # Tracks how many courses we have successfully taken
        while zeroDegreeQueue:
            course = zeroDegreeQueue.popleft()
            count += 1  # One more course has been processed

            for neighbor in adjList[course]:
                inDegree[neighbor] -= 1  # Remove edge
                if inDegree[neighbor] == 0:  # If no remaining prerequisites, add to queue
                    zeroDegreeQueue.append(neighbor)

        # Step 4: If we processed all courses, return True; otherwise, cycle exists
        return count == numCourses

# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         """
#         Determines if all courses can be finished using DFS cycle detection.

#         Args:
#             numCourses: Total number of courses.
#             prerequisites: List of prerequisite pairs [a, b] where b → a.

#         Returns:
#             True if all courses can be completed, False if there is a cycle.

#         Time Complexity: O(V + E) (DFS processes each node and edge once)
#         Space Complexity: O(V + E) (for adjList space)
#         """

#         # create adjacent list with reversed edges
#         adjList = [[] for _ in range(numCourses)] 
#         inDegrees = [0 for _ in range(numCourses)]

#         # populate reverse adjList and count degrees
#         for connectedNodes in prerequisites:

#             adjList[connectedNodes[0]].append(connectedNodes[1]) # reverse edge
#             inDegrees[connectedNodes[1]] += 1
        
#         # Establish stack of nodes with zero indegrees
#         zeroStack = deque()
#         for i in range(len(inDegrees)):
#             if inDegrees[i] == 0:
#                 zeroStack.append(i)

#         # tracked visited safeNodes
#         visited = set()
#         pendingVisit = set(range(numCourses))
#         while zeroStack:

#             safeNode = zeroStack.popleft()

#             if safeNode in visited:
#                 return False # cycle detected, course cannot be completed
            
#             pendingVisit.remove(safeNode)
#             visited.add(safeNode)
            
#             for node in adjList[safeNode]:
#                 inDegrees[node] -= 1

#                 if inDegrees[node] == 0:
#                     zeroStack.append(node)
        
#         return True if visited and not pendingVisit else False# course can be completed
        

            

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