import unittest
from collections import defaultdict, deque

class Solution:
    def allCourseOrders(self, numCourses: int, prerequisites: list[list[int]]) -> list[list[int]]:
        """return all possible order that you can take the course
        TC O(K * (V + E))
        SC O(K * V + V + E)
        """
        
        # must explore all paths so DFS will be better approach
        
        # create inDegree and adjList Graph
        inDegree = defaultdict(int)
        for num in range(numCourses): # O(n) SC and TC
            inDegree[num] = 0
            # indegree here is used as a prunning method to avoid computing 
            # invalid paths
            
        digraph = defaultdict(list)
        for nextCourse, priorCourse in prerequisites:
            digraph[priorCourse].append(nextCourse)
            inDegree[nextCourse] += 1
        
        visited, allCourseOrders = set(), []
        
        def dfs(currOrder):
            if len(currOrder) == numCourses:
                allCourseOrders.append(currOrder[:])
                return
            
            for course in range(numCourses):
                if inDegree[course] == 0 and course not in visited:
                    # choose if there is not indegree (already determined above)
                    visited.add(course)
                    currOrder.append(course)
                    for neighbor in digraph[course]:
                        inDegree[neighbor] -= 1

                    # explore
                    dfs(currOrder)

                    # un-choose (backtrack)
                    for neighbor in digraph[course]:
                        inDegree[neighbor] += 1
                    currOrder.pop()
                    visited.remove(course)

        dfs([])
        
        return allCourseOrders
        

class TestAllCourseOrders(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        numCourses = 2
        prerequisites = [[1, 0]]
        expected = [[0, 1]]
        result = self.sol.allCourseOrders(numCourses, prerequisites)
        self.assertCountEqual(result, expected)

    # def test_example_2(self):
    #     numCourses = 4
    #     prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    #     expected = [
    #         [0,1,2,3],
    #         [0,2,1,3]
    #     ]
    #     result = self.sol.allCourseOrders(numCourses, prerequisites)
    #     self.assertCountEqual(result, expected)

    # def test_no_prerequisites(self):
    #     numCourses = 3
    #     prerequisites = []
    #     result = self.sol.allCourseOrders(numCourses, prerequisites)
    #     expected = [
    #         [0,1,2], [0,2,1],
    #         [1,0,2], [1,2,0],
    #         [2,0,1], [2,1,0]
    #     ]
    #     self.assertCountEqual(result, expected)

    # def test_cycle(self):
    #     numCourses = 2
    #     prerequisites = [[0, 1], [1, 0]]
    #     result = self.sol.allCourseOrders(numCourses, prerequisites)
    #     expected = []
    #     self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()