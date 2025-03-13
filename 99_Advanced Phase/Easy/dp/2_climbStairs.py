class Solution:
    def climbStairs(self, n: int) -> int:
        """
        return distinct way to climb the stairs
        """
        
        pass


import unittest

class TestSolution(unittest.TestCase):
    def test_climbStairs(self):
        sol = Solution()
        
        # Base cases
        self.assertEqual(sol.climbStairs(1), 1)
        self.assertEqual(sol.climbStairs(2), 2)

        # Small cases
        self.assertEqual(sol.climbStairs(3), 3)
        self.assertEqual(sol.climbStairs(4), 5)
        self.assertEqual(sol.climbStairs(5), 8)

        # Larger cases
        self.assertEqual(sol.climbStairs(10), 89)
        self.assertEqual(sol.climbStairs(20), 10946)

        # Upper bound case
        self.assertEqual(sol.climbStairs(45), 1836311903)

if __name__ == "__main__":
    unittest.main()