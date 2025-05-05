import unittest

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        """
        return output of RPN - 
        Potential edge case that problem does not clarify on - what to return
        if len(tokens) == 1 but tokens[0] is an operator? Assume 0? Though it
        states that input will be a valid expression of RPN so I assume we will 
        ok.
        
        TC and SC = O(n)
        """
        
        operator = {
            '*' : lambda a, b: a * b,
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '/': lambda a, b: int(a / b) # truncate towards 0
        }
        
        arith = []
        
        for str in tokens:
        
            if str not in operator:
                arith.append(int(str))
            
            else:
                b = arith.pop()
                a = arith.pop()
                result = operator[str](a, b)
                
                arith.append(result)
            
        return arith[0]
        
        


class TestEvalRPN(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        tokens = ["2", "1", "+", "3", "*"]
        self.assertEqual(self.sol.evalRPN(tokens), 9)

    def test_example2(self):
        tokens = ["4", "13", "5", "/", "+"]
        self.assertEqual(self.sol.evalRPN(tokens), 6)

    def test_example3(self):
        tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        self.assertEqual(self.sol.evalRPN(tokens), 22)

    def test_single_number(self):
        tokens = ["42"]
        self.assertEqual(self.sol.evalRPN(tokens), 42)

    def test_negative_division(self):
        tokens = ["-4", "2", "/"]
        self.assertEqual(self.sol.evalRPN(tokens), -2)

    def test_large_expression(self):
        tokens = ["3", "4", "+", "2", "*", "7", "/"]
        self.assertEqual(self.sol.evalRPN(tokens), 2)

    def test_subtraction(self):
        tokens = ["5", "1", "-"]
        self.assertEqual(self.sol.evalRPN(tokens), 4)


if __name__ == "__main__":
    unittest.main() 
    