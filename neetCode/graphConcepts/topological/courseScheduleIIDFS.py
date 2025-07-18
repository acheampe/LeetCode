import unittest
from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        """return a list of a possible order in which you can complete a course.
        if unable return an empty list
        TC and SC == O(V + E)
        """
        
        def example():
            """numCourses = 2
            preq = [[0,1]] 
            so as a digraph i would get something like this:
            1 --> 0, thus one indegree (at least one course is req before taking course 0)
            
            Questions prior to approach:
            can I assume that numCourses and preq input will match up? 
            for example could preq = [[0]] and numCourse = 2? if so then I can 
            use an assert to guard against this.
            """
            pass
        
        # DFS approach
        # graph to turn input preq into an adjacent list
        digraph = defaultdict(list)
        for course, preq in prerequisites:
            digraph[preq].append(course)
            
        visited, currPath, courseOrder = set(), set(), []
        
        def isCycle(course):
            # establish base cases
            if course in currPath:
                return True
            
            if course in visited:
                return False
            
            currPath.add(course)
            for allowedCourse in digraph[course]:
                if isCycle(allowedCourse):
                    return True

            # [blocker] remember once you get past loop point, it means exploration was a valid path, else it would have
            # detected a cycle earlier
            visited.add(course)
            currPath.remove(course)
            courseOrder.append(course)
            return False
        
        for pre in range(numCourses): # major blocker here is using numCourse range instead of iter over key of graph for disconnected graph
            if pre not in visited:
                if isCycle(pre):
                    return []
                    
        return courseOrder[::-1] # result is returned in postorder (child node appended first before parent node, thus the reversal)
    
class TestCourseScheduleII(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_simple_case(self):
        numCourses = 2
        prerequisites = [[1, 0]]
        res = self.sol.findOrder(numCourses, prerequisites)
        self.assertEqual(res, [0, 1])

    def test_simple_case2(self):
        numCourses = 2
        prerequisites = [[0,1]]
        res = self.sol.findOrder(numCourses, prerequisites)
        self.assertEqual(res, [1,0])
        
    def test_multiple_valid_orders(self):
        numCourses = 4
        prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
        res = self.sol.findOrder(numCourses, prerequisites)
        self.assertTrue(res in [[0,1,2,3], [0,2,1,3]])

    def test_single_course(self):
        numCourses = 1
        prerequisites = []
        self.assertEqual(self.sol.findOrder(numCourses, prerequisites), [0])

    def test_impossible_case_due_to_cycle(self):
        numCourses = 2
        prerequisites = [[0, 1], [1, 0]]
        self.assertEqual(self.sol.findOrder(numCourses, prerequisites), [])

    def test_disconnected_courses(self):
        numCourses = 3
        prerequisites = [[1, 0]]
        res = self.sol.findOrder(numCourses, prerequisites)
        self.assertTrue(res in [[0,1,2], [2,0,1]])

if __name__ == '__main__':
    unittest.main()