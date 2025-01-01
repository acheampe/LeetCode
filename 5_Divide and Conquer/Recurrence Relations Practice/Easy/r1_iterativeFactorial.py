from typing import List

def find_factorial(n: int) -> int:
    """
    return factorial of n
    """

    #iterative approach 

    result = 1 # for edge case of n = 0 and for multiplicity

    for i in range(1, n + 1): # for inclusive n
        result *= i
    
    return result  # TC = O(n) and SC = O(1)


sol = find_factorial
# Test Case 1 
print(sol(0))  # Expected Output: 1

# # Test Case 2
# print(sol(1))  # Expected Output: 1

# # Test Case 3
# print(sol(5))  # Expected Output: 120

# # Test Case 4
# print(sol(10))  # Expected Output: 3628800

# # Test Case 5
# print(sol(20))  # Expected Output: 2432902008176640000