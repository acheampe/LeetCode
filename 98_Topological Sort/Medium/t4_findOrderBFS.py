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

        # create adjacent list and inDegree list
        adjList =[[] for _ in range(numCourses)]
        inDegree = [0] * numCourses

        # Populate adjacent list
        for courses in prerequisites:
            adjList[courses[-1]].append(courses[0])
            inDegree[courses[0]] += 1 
        
        zeroDeque = deque()

        for i in range(numCourses):
            if inDegree[i] == 0:
                zeroDeque.append(i)
        
        count = 0 # track number zero Degree nodes processed
        orderedResult = []
        while zeroDeque:

            validCourse = zeroDeque.popleft()
            orderedResult.append(validCourse)
            count += 1

            for node in adjList[validCourse]:

                inDegree[node] -= 1

                if inDegree[node] == 0:
                    zeroDeque.append(node)
        
        return orderedResult if count == numCourses else []


class TestFindOrder(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()  # Assuming the Solution class is correctly implemented

    def test1(self):
        numCourses = 2
        prerequisites = [[1, 0]]
        output = [0, 1]  # One valid order
        self.assertIn(self.sol.findOrder(numCourses, prerequisites), [[0, 1]])

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

    def test4(self):  # No prerequisites, multiple courses
        numCourses = 3
        prerequisites = []
        output1 = [0, 1, 2]
        output2 = [1, 2, 0]
        output3 = [2, 0, 1]  # Any order is valid
        self.assertIn(self.sol.findOrder(numCourses, prerequisites), [output1, output2, output3])

    def test5(self):  # Cycle in prerequisites
        numCourses = 2
        prerequisites = [[1, 0], [0, 1]]
        output = []
        self.assertEqual(self.sol.findOrder(numCourses, prerequisites), output)

    # def test6(self):  # Multiple courses with independent chains
    #     numCourses = 5
    #     prerequisites = [[1, 0], [3, 2], [4, 3]]
    #     output1 = [0, 1, 2, 3, 4]
    #     output2 = [2, 3, 4, 0, 1]  # Both are valid
    #     self.assertIn(self.sol.findOrder(numCourses, prerequisites), [output1, output2])

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

    def test10(self):  # Stress test with large input, no cycles
        numCourses = 2000
        prerequisites = [[i + 1, i] for i in range(1999)]  # Linear dependency
        output = list(range(2000))
        self.assertEqual(self.sol.findOrder(numCourses, prerequisites), output)

    # def test12(self): 
    #     numCourses = 5 
    #     prerequisites = [[1,4],[2,4],[3,1],[3,2]]
    #     output = True
    #     self.assertEqual(self.sol.canFinish(numCourses, prerequisites), output)

if __name__ == '__main__':
    unittest.main()