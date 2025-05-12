import unittest

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        """generate all possible parenthesis
        TC: O(4^n / sqrt(n)) — Catalan number growth
        SC: O(n) for recursion stack + O(4^n / sqrt(n)) for result storage
        """
        
        result = []
        stack = []
        def backtracking(openCount, closeCount):
            
            if openCount == closeCount == n:
                result.append("".join(stack))
                return
            
            if openCount < n:
                stack.append("(")
                backtracking(openCount + 1, closeCount)
                stack.pop()
            
            if closeCount < openCount:
                stack.append(")")
                backtracking(openCount, closeCount + 1)
                stack.pop()
        
        backtracking(0, 0)
        return result
        
        
        

class TestGenerateParenthesis(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_n_is_1(self):
        result = self.solution.generateParenthesis(1)
        expected = ["()"]
        self.assertCountEqual(result, expected)

    def test_n_is_2(self):
        result = self.solution.generateParenthesis(2)
        expected = ["(())", "()()"]
        self.assertCountEqual(result, expected)

    def test_n_is_3(self):
        result = self.solution.generateParenthesis(3)
        expected = ["((()))", "(()())", "(())()", "()(())", "()()()"]
        self.assertCountEqual(result, expected)

    def test_n_is_0(self):
        result = self.solution.generateParenthesis(0)
        expected = [""]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()