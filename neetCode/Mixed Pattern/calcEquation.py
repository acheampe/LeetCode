from collections import deque, defaultdict
import unittest

class Solution:
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(dict)

        # Step 1: Build the graph
        for (num, den), val in zip(equations, values):
            graph[num][den] = val
            graph[den][num] = 1 / val

        def bfs(start, end):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0

            visited = set()
            queue = deque([(start, 1.0)])  # (current_node, cumulative_product)

            while queue:
                curr, prod = queue.popleft()

                if curr == end:
                    return prod

                visited.add(curr)

                for neighbor, val in graph[curr].items():
                    if neighbor not in visited:
                        queue.append((neighbor, prod * val))

            return -1.0

        # Step 2: Handle each query with BFS
        results = []
        for a, b in queries:
            results.append(bfs(a, b))

        return results
    

class TestCalcEquation(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        equations = [["a", "b"], ["b", "c"]]
        values = [2.0, 3.0]
        queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
        expected = [6.0, 0.5, -1.0, 1.0, -1.0]
        result = self.sol.calcEquation(equations, values, queries)
        for r, e in zip(result, expected):
            self.assertAlmostEqual(r, e)

    # def test_example_2(self):
    #     equations = [["a", "b"], ["b", "c"], ["bc", "cd"]]
    #     values = [1.5, 2.5, 5.0]
    #     queries = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
    #     expected = [3.75, 0.4, 5.0, 0.2]
    #     result = self.sol.calcEquation(equations, values, queries)
    #     for r, e in zip(result, expected):
    #         self.assertAlmostEqual(r, e)

    # def test_example_3(self):
    #     equations = [["a", "b"]]
    #     values = [0.5]
    #     queries = [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]
    #     expected = [0.5, 2.0, -1.0, -1.0]
    #     result = self.sol.calcEquation(equations, values, queries)
    #     for r, e in zip(result, expected):
    #         self.assertAlmostEqual(r, e)


if __name__ == '__main__':
    unittest.main()