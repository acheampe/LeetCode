from typing import List

def find_factorial(n: int) -> int:
    """
    return factorial of n
    """

    # Egde and termination case
    if n <= 1:
        return 1
    
    return n * find_factorial(n - 1) # TC = O(n) and SC = O(n) due to stack used

# Recurrence Relations
# T(n) {n = 1, constant, n*T(n-1)}


sol = find_factorial
# Test Case 1
print(sol(0))  # Expected Output: 1

# Test Case 2
print(sol(1))  # Expected Output: 1

# Test Case 3
print(sol(5))  # Expected Output: 120

# Test Case 4
print(sol(10))  # Expected Output: 3628800

# Test Case 5
print(sol(20))  # Expected Output: 2432902008176640000