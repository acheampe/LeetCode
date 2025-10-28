import unittest
from collections import defaultdict

from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # example:
        # [[0, 1], [1, 2], [3, 1]]
        #{0: [1]; 1: [3]; 2: [1]}
        # 1 -> 0
        # 2 -> 1
        # 1 -> 3 # no cycle
        # if we added [2, 3], 3 -> 2 -> 1 -> 3 cycle will be detected


        # since prereq input is in no indexed order, where index zero == course 0, the best course of action will be to use adjlist to help navigate path
        # path example: {0 - > 1 - > 3}
        adjList: defaultdict[int, list] = defaultdict(list) # SC O(n) n == (numCourses - 1) + Edge in worse case
        isCycleMemo: dict[int, bool] = {} #optimize path tracing to reduce repetitive pathfinding - SC O(n), n == numCourses - 1 in worse case

        for course, preq in prerequisites:
            adjList[preq].append(course)

        def isCycle(courseNum: int, currPath: set) -> bool:
            
                if courseNum in isCycleMemo:
                    return isCycleMemo[courseNum] # returns False
                
                if courseNum in currPath:
                    return True # cycle detected
                
                currPath.add(courseNum)
                for course in adjList[courseNum]:
                    if isCycle(course, currPath):
                        return True
                    
                currPath.remove(courseNum)
                isCycleMemo[courseNum] = False

                return False

        for i in range(numCourses):
            coursePath: set[int] = set()
            if isCycle(i, coursePath):
                return False
        
        return True
        # Overall TC: O(n), n == numCourses - 1 + E (edges)
        # Overall SC: O(n), for recursion path considering memoization
# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        
#         # turn list datastruct to adjlist
#         graph = defaultdict(list) # O(V + E) space

#         for course, prereq in prerequisites:
#             graph[prereq].append(course)
        
#         # declare visited and currPath DS as set
#         visited, currPath = set(), set() # O(V + E) space

#         def isCycle(currCourse):
            
#             # Establish base cases here:
#             if currCourse in currPath:
#                 return True # Cycle exist in this currPath

#             if currCourse in visited:
#                 return False # wanna avoid redoing work already done
            
#             currPath.add(currCourse)

#             for nextCourse in graph[currCourse]: # TC O(V + E)
#                 if isCycle(nextCourse):
#                     return True
            
#             currPath.remove(currCourse)
#             visited.add(currCourse)
#             return False

#         for course in range(numCourses): # O(V + E) TC
#             #only explore courses that have not been explored
#             if course not in visited:
#                 if isCycle(course):
#                     return False
#         # if no cycle is detected
#         return True
                

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