import unittest
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)

        visited = set()
        currPath = set()

        def isCycle(course):
            if course in currPath:
                return True  # cycle found
            if course in visited:
                return False  # already processed and no cycle

            currPath.add(course)
            for neighbor in graph[course]:
                if isCycle(neighbor):
                    return True
            currPath.remove(course)
            visited.add(course)
            return False

        for course in range(numCourses):  # important: cover disconnected nodes
            if isCycle(course):
                return False  # cycle detected

        return True

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