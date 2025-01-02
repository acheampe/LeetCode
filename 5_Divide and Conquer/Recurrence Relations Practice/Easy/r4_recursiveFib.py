class Solution:
    def fib(self, n: int) -> int:
        """
        return the appropriate output bases on fibonacci number
        """

        # Base/termination case:
        if n <= 1:
            return 1

        result = self.fib(n - 1) + self.fib(n - 2) # TC = O(n) and SC = O(n) for stack use
        
        return result
    

sol = Solution()
print(sol.fib(2)) # Expected Output = 1
# print(sol(3)) # Expected Output = 2
# print(sol(4)) # Expected Output = 3