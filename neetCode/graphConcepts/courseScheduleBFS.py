import unittest
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        
        visited = set()
        currPath = set()
        graph = defaultdict(list)

        for arr in prerequisites:
            graph[arr[1]].append(arr[0])
        
        def cycle(course):
            
            if course in currPath:
                return True # there is a cycle
            
            if course in visited: 
                return False # previously explored path with no cycle 
            
            currPath.add(course)
            visited.add(course)
            for nextCourse in graph[course]:
                if nextCourse not in visited:
                    if cycle(nextCourse):
                        return True
                
            currPath.remove(course)
            visited.add(course) # added after it's whole path is proven acyclic. 
            return False
        
        for course in range(numCourses):
            if course not in visited:
                if cycle(course): # if true that there is a cycle
                    return False # cycle detected

        return True # course can be completed

class TestCourseSchedule(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        self.assertTrue(self.sol.canFinish(2, [[1, 0]]))

    def test_example_2(self):
        self.assertFalse(self.sol.canFinish(2, [[1, 0], [0, 1]]))

    def test_disconnected_components(self):
        self.assertTrue(self.sol.canFinish(4, [[1, 0], [2, 3]]))

    def test_large_acyclic(self):
        self.assertTrue(self.sol.canFinish(5, [[1, 0], [2, 1], [3, 2], [4, 3]]))

    def test_self_dependency(self):
        self.assertFalse(self.sol.canFinish(1, [[0, 0]]))

    def test_no_prerequisites(self):
        self.assertTrue(self.sol.canFinish(3, []))

    def test_multiple_cycles(self):
        self.assertFalse(self.sol.canFinish(4, [[0,1],[1,2],[2,3],[3,1]]))

if __name__ == "__main__":
    unittest.main()