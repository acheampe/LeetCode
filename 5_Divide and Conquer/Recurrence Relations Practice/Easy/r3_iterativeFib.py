class Solution:
    def fib(self, n: int) -> int:
        """
        return the appropriate output bases on fibonacci number
        """

        currResult = [0, 1] # for established base rule
        startIndex = 0

        while startIndex < n:
            if startIndex != n:
                currResult.append(currResult[len(currResult) - 2] + currResult[len(currResult) - 1])
            startIndex += 1
        
        return currResult[n] # TC and SC = O(n)
        

            
sol = Solution()
print(sol.fib(2)) # Expected Output = 1
print(sol.fib(3)) # Expected Output = 2
print(sol.fib(4)) # Expected Output = 3