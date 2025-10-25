import unittest

class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        # TC O(n * V + E) n == number of queries
        # SC O(V + E) for adj list * h (recursion depth)
        result: list[float] = [-1.0 for _ in range(len(queries))]
        graph: dict[str, dict[str, float]] = {}
        m: int = len(equations)
        
        for i in range(m):
            num, den = equations[i]
            weight: float = values[i]
            if num not in graph:
                graph[num] = {}
            if den not in graph:
                graph[den] = {}
            graph[num][den] = weight
            graph[den][num] = (1/weight)
        
        def findProduct(src, target, currProduct, visited) -> float | None:
            
            if src not in graph or target not in graph:
                return None
            
            if target in graph[src].keys():
                return currProduct * graph[src][target]
            
            if target == src:
                return currProduct

            visited.add(src)
            for key, val in graph[src].items():
                if key not in visited:
                    queryProduct = findProduct(key, target, val * currProduct, visited)
                    if queryProduct is not None:
                        return queryProduct
            
            return None
        
        for i in range(len(queries)):
            visited: set[int] = set()
            num, den = queries[i]
            product = findProduct(num, den, 1, visited)
            if product:
                result[i] = product

        return result
    
class TestCalcEquation(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        equations = [["a", "b"], ["b", "c"]]
        values = [2.0, 3.0]
        queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
        expected = [6.0, 0.5, -1.0, 1.0, -1.0]
        result = self.s.calcEquation(equations, values, queries)
        for r, e in zip(result, expected):
            self.assertAlmostEqual(r, e, places=5)

    def test_example2(self):
        equations = [["a", "b"], ["b", "c"], ["bc", "cd"]]
        values = [1.5, 2.5, 5.0]
        queries = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
        expected = [3.75, 0.4, 5.0, 0.2]
        result = self.s.calcEquation(equations, values, queries)
        for r, e in zip(result, expected):
            self.assertAlmostEqual(r, e, places=5)

    def test_example3(self):
        equations = [["a", "b"]]
        values = [0.5]
        queries = [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]
        expected = [0.5, 2.0, -1.0, -1.0]
        result = self.s.calcEquation(equations, values, queries)
        for r, e in zip(result, expected):
            self.assertAlmostEqual(r, e, places=5)

if __name__ == "__main__":
    unittest.main() 