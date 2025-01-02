class Solution:
    def fib(self, n: int) -> int:
        """
        return the appropriate output bases on fibonacci number
        """

        # Base/termination case:
        if n == 0 or n == 1:
            return 1 if n == 1 else 0
        
        return self.fib(n - 1) + self.fib(n - 2) # TC = O(2^n) and SC = O(n) for stack use - try with memoization when you get to DP
    
    # Recurrence relations: T(n) = T(n - 1) + T(n - 2)
    

sol = Solution()
print(sol.fib(2)) # Expected Output = 1
print(sol.fib(3)) # Expected Output = 2
print(sol.fib(4)) # Expected Output = 3