from typing import List
# ## 1652. Defuse the Bomb

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        """
        find sum of k window and place in respective index
        """

        arrLen = len(code)
        decryptedCode = [0] * arrLen

        if k == 0:
            return decryptedCode
        
        # Sets up iteration logic // exclusive end var
        start, end, step = (1, k + 1, 1) if k > 0 else (arrLen + k, arrLen, 1)

        # Calc. current window
        currWindowVal = sum(code[i % arrLen] for i in range (start, end, step))

        # Place iterative sum in respective index
        for i in range(arrLen):
            decryptedCode[i] = currWindowVal

            # calc drop and added val based on index
            dropVal = code[(start + i) % arrLen]
            addVal = code[(end + i) % arrLen]

            currWindowVal -= dropVal
            currWindowVal += addVal
        
        return decryptedCode
 
sol = Solution()
# first_dec = sol.decrypt([5,7,1,4], 3)
# print(first_dec)
fourth_dec = sol.decrypt([5,2,2,3,1], 3)
print(fourth_dec)
# Expected
[7,6,9,8,9]
# Expected
# [12,10,16,13]
# sec_dec = sol.decrypt([2,4,9,3], -2)
# print(sec_dec)
# third_dec = sol.decrypt([10,5,7,7,3,2,10,3,6,9,1,6], -4)
# print(third_dec)
# Output
# [3,9,10,8]
# Expected
# [12,5,6,13]



# class Solution:
#     def decrypt(self, code: List[int], k: int) -> List[int]:
#         """
#         To determine the sum of curr window size k and place in respective
#         index determine by pos/neg k val
#         """

#         # Establish variables
#         arrlen = len(code) # length of array
#         absK = abs(k) # ensure positive val of k when needed
#         decryptCode = [0 for i in range(arrlen)] # initialize newArr with 0s
#         currSum = sum(code[:absK]) # absolute k here

#         for i in range(arrlen):

#             # Address neg k condition
#             if k < 0:   # we want k, not absK to determine neg or pos val
#                 if i == 0:
#                     decryptCode[absK] = currSum
            
#                 else:
#                     currSum = currSum - code[(i  - 1) % arrlen] + code[(absK + i - 1) % arrlen]
#                     decryptCode[(k + i )% arrlen] = currSum # pythonic use - modulo
            
#             # Address pos k condition
#             if k > 0:
#                 if i == 0:
#                     decryptCode[arrlen - 1] = currSum
                
#                 else:
#                     currSum = currSum - code[(i - 1) % arrlen] + code[(k + i - 1) % arrlen]
#                     decryptCode[(i - 1) % arrlen] = currSum
            
#         return decryptCode 

# from typing import List

# class Solution:
#     def decrypt(self, code: List[int], k: int) -> List[int]:
#         n = len(code)
        
#         # If k is zero, return an array of zeros
#         if k == 0:
#             return [0] * n
        
#         # Initialize variables
#         decodedArr = [0] * n
        
#         start, end, step = (1, k, 1) if k > 0 else (n - 1, n + k - 1, -1)
        
#         # Calculate the initial sum for the first window
#         window_sum = sum(code[i % n] for i in range(start, end + 1, step))
        
#         for i in range(n):
#             # Assign the current window sum
#             decodedArr[i] = window_sum
            
#             # Update the window sum for the next iteration
#             window_sum -= code[(start + i) % n]
#             window_sum += code[(end + i + 1) % n]
        
#         return decodedArr
