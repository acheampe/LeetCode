import unittest
from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        """return a list of a possible order in which you can complete a course.
        if unable return an empty list
        TC and SC == O(V + E)
        """
        
        inDegree = defaultdict(int)
        for num in range(numCourses):
            inDegree[num] = 0
        
        # create adjList and inDegree
        digraph = defaultdict(list)
        for course, pre in prerequisites: # O(V + E)
            inDegree[course] += 1
            digraph[pre].append(course)
        
        deStack = deque()
        
        for course in inDegree: # O(n)
            if inDegree[course] == 0: 
                deStack.append(course)
                
        courseOrder = []
                
        while deStack:
            pre = deStack.popleft()
            courseOrder.append(pre)
            
            for course in digraph[pre]:
                # we have one less in degree now
                inDegree[course] -= 1
                
                if inDegree[course] == 0:
                    deStack.append(course)
        
        return courseOrder
                
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