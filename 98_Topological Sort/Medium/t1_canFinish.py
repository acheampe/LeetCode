from typing import List
import unittest

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pass


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

    def test3(self):  # No prerequisites (Minimum Constraint)
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

if __name__ == '__main__':
    unittest.main()