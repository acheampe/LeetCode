import unittest

class Solution:
    def climbStairs(self, n: int) -> int:
        """
        return all distinct ways to be able to climb given stairs with n steps to reach the top
        
        TC: O(n) for recursive and iter approach
        Sc: O(n) memo + recur stack, O(1) for iter approach
        """
        ## Recursive approach
        # memo = {}
        # def dfs(total):
        #     """ 
        #     return count, count tracks distinct ways to reach the top
        #     """
        #     if total in memo:
        #         return memo[total]
        #     if total == 0 or total == 1:
        #         return 1
            
        #     memo[total] = dfs(total - 2) + dfs(total - 1)
            
        #     return memo[total]
            
        
        # return dfs(n)
        
        # Iterative approach
        
        # base Cases
        if n == 0:
            return 1
        prev2, prev1 = 1, 1
        
        for _ in range(2, n + 1): # inclusive n
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr
        
        return prev1

def climbing_stairs_summary():
    """
    Returns a summary of different approaches to solving the Climbing Stairs problem.
    """

    summary = """
    Climbing Stairs Problem Summary:
    
    The problem follows a Fibonacci-like recurrence relation:
    f(n) = f(n-1) + f(n-2)
    
    Since each step can be reached from either (n-1) or (n-2), we can solve it using:
    
    1️⃣ **Recursive Approach (Naive)**
       - Directly uses the recurrence relation.
       - Time Complexity: O(2^n) (exponential, slow for large n).
       - Space Complexity: O(n) (recursion stack depth).
       - Not practical for large n.

    2️⃣ **Recursive Approach with Memoization (Top-Down DP)**
       - Stores computed values in a dictionary (memoization).
       - Time Complexity: O(n) (each subproblem computed once).
       - Space Complexity: O(n) (recursion stack + memo dictionary).
       - Optimizes the naive recursion approach.

    3️⃣ **Iterative Dynamic Programming (Bottom-Up DP)**
       - Uses an array to store results from 0 to n.
       - Time Complexity: O(n).
       - Space Complexity: O(n) (due to array storage).
       - Works well but uses extra space.

    4️⃣ **Iterative Optimized (Constant Space)**
       - Stores only the last two values (prev1, prev2) to compute the next.
       - Time Complexity: O(n).
       - Space Complexity: O(1) (only two variables used).
       - Most efficient solution.
    
    🏆 **Recommended Approach**:
       ✅ The Iterative Optimized Approach (O(n) time, O(1) space) is the best for large values of n.
    
    🔥 Bonus: The problem is a Fibonacci variant, so similar approaches apply to problems like:
       - Frog Jump (can jump 1, 2, or k steps).
       - Tiling Problems (ways to fill an n×2 board with 1×2 tiles).
       - Counting valid binary strings (no consecutive 1s).
    """
    
    return summary

# Example usage:
print(climbing_stairs_summary())
            
    

class TestSolution(unittest.TestCase):
    def test_climbStairs(self):
        sol = Solution()
        
        # Base cases
        # self.assertEqual(sol.climbStairs(1), 1)
        # self.assertEqual(sol.climbStairs(2), 2)

        # Small cases
        self.assertEqual(sol.climbStairs(3), 3)
        # self.assertEqual(sol.climbStairs(4), 5)
        # self.assertEqual(sol.climbStairs(5), 8)

        # # Larger cases
        # self.assertEqual(sol.climbStairs(10), 89)
        # self.assertEqual(sol.climbStairs(20), 10946)

        # # Upper bound case
        self.assertEqual(sol.climbStairs(45), 1836311903)

if __name__ == "__main__":
    unittest.main()