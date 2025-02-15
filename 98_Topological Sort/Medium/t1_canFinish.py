from typing import List
import unittest

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        func to decide if all courses can be finished

        Args: Int --> number of courses; Prereq --> List of courses

        Return: Bool                                                                                                                                                                             

        Time Complexity: O(n) for iter through prereqs
        Space Complexity: O(n) for inDegree
        """

        # Address Edge Case:
        if not prerequisites:
            return True # No prereqs needed to complete number of courses 
 
        inDegree = [0] * numCourses # to coubt inDegrees
        trackDuplicate = set() # if duplicate tuple is seen, then unable to complete all courses

        for courses in prerequisites: # O(n) Operation

            #count inDegree
            inDegree[courses[0]] += 1

            # if inDegree[courses[0]] == 2:
            #     return False # Early Cycle detection

            if courses[0] > courses[1]: # O(1) operation
                courses[0], courses[1] = courses[1], courses[0]
            if tuple(courses) in trackDuplicate or courses[0] == courses[1]: # avoid self loop or duplicate
                return False
            else:
                trackDuplicate.add(tuple(courses))
        
        for edge in inDegree:
            if edge ==  0:
                return True # No cycle all courses can be taken
        
        return False # All ones in inDegree

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