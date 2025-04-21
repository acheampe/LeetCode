import unittest

class Solution:
    def isValid(self, s: str) -> bool:
        """return true if parentheses are in valid order"""
    
        def discussApproach():
            """
            First thought is to use a two pointer system but this approach exposes 
            a weakness that will be near improbable to catch all edge cases without 
            verbose conditions

            The minimun length of s is 1 so no need to worry about empty input cases.
            We can use a stack operation to compare current iteration of chr to last append value to
            see if there is a match, this will be O(n) TC and SC
            """
        
        def isParenthesis(firstParenthesis, secondParenthesis):
            """return bool if brackets are appropriately paired or not"""

            isMatch = (
                (firstParenthesis, secondParenthesis) == ('(', ')') or
                (firstParenthesis, secondParenthesis) == ('[', ']') or
                (firstParenthesis, secondParenthesis) == ('{', '}')
            )

            return isMatch
        
        stack = []
        for i in range(len(s)):

            if stack:
                print(isParenthesis(stack[-1], s[i]))
                if isParenthesis(stack[-1], s[i]):
                    stack.pop()
                    continue

            stack.append(s[i])
        
        return not stack


class TestValidParentheses(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        self.assertTrue(self.sol.isValid("()"))

    def test_example_2(self):
        self.assertTrue(self.sol.isValid("()[]{}"))

    def test_example_3(self):
        self.assertFalse(self.sol.isValid("(]"))

    def test_example_4(self):
        self.assertTrue(self.sol.isValid("([])"))

    def test_nested_mismatch(self):
        self.assertFalse(self.sol.isValid("([)]"))

    def test_only_opening(self):
        self.assertFalse(self.sol.isValid("((("))

    def test_only_closing(self):
        self.assertFalse(self.sol.isValid("]]]"))

    def test_mixed_unbalanced(self):
        self.assertFalse(self.sol.isValid("{[}"))

    def test_empty_string(self):
        self.assertTrue(self.sol.isValid(""))

    def test_long_valid(self):
        self.assertTrue(self.sol.isValid("({[]})[{}]({()})"))

    def test_long_invalid(self):
        self.assertFalse(self.sol.isValid("({[]})[{}]({()})]("))

if __name__ == '__main__':
    unittest.main()