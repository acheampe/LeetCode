import unittest
from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
    
        graph = defaultdict(list)
        inDegree = {
            
        }
        stack = deque()
        
        for a, b in prerequisites:
            graph[b].append(a)
        
        for course in graph:
            inDegree[course] = 0
            for _ in graph[course]:
                inDegree[course] += 1
        
        for course, preq in inDegree.items():
            if preq == 0:
                stack.append(course)
        
        while stack:
            pass
                
                
            
            
            
            
        
      

class TestCourseSchedule(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        self.assertTrue(self.sol.canFinish(2, [[1, 0]]))

    # def test_example_2(self):
    #     self.assertFalse(self.sol.canFinish(2, [[1, 0], [0, 1]]))

    # def test_disconnected_components(self):
    #     self.assertTrue(self.sol.canFinish(4, [[1, 0], [2, 3]]))

    # def test_large_acyclic(self):
    #     self.assertTrue(self.sol.canFinish(5, [[1, 0], [2, 1], [3, 2], [4, 3]]))

    # def test_self_dependency(self):
    #     self.assertFalse(self.sol.canFinish(1, [[0, 0]]))

    # def test_no_prerequisites(self):
    #     self.assertTrue(self.sol.canFinish(3, []))

    # def test_multiple_cycles(self):
    #     self.assertFalse(self.sol.canFinish(4, [[0,1],[1,2],[2,3],[3,1]]))

if __name__ == "__main__":
    unittest.main()