from typing import List
import unittest

class Solution:
    def fib(self, n: int) -> int:
        
        memo = {
            0 : 0,
            1 : 1
        } # to store calc vals

        def dp(m: int) -> int:

            # termination case:
            if m in memo:
                return memo[m]
            
            memo[m] = dp(m - 1) + dp(m - 2)
            return memo[m]
        
        return dp(n)

class TestSolution(unittest.TestCase):
    def test_fib(self):
        sol = Solution()
        
        # Base cases
        self.assertEqual(sol.fib(0), 0)
        self.assertEqual(sol.fib(1), 1)
        
        # Small Fibonacci numbers
        self.assertEqual(sol.fib(2), 1)
        self.assertEqual(sol.fib(3), 2)
        self.assertEqual(sol.fib(4), 3)
        self.assertEqual(sol.fib(5), 5)

        # Larger Fibonacci numbers
        self.assertEqual(sol.fib(10), 55)
        self.assertEqual(sol.fib(15), 610)


if __name__ == "__main__":
    unittest.main()