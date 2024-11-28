from typing import List
# ## 1652. Defuse the Bomb

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

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:

        #length of code
        arrLength = len(code)

        # Initialize decodedArr
        decodedArr = [0] * arrLength

        # edge case k == 0
        if k == 0:
            return decodedArr
        
        # Iteration condition based on k value
        start, end, step = (1, k, 1) if k > 0 else (arrLength - 1, arrLength + k - 1, -1)

        # Calculate current window sum
        windowSum = sum(code[i % arrLength] for i in range(start, end + 1, step))

        # Calculate sum of respective index
        for i in range(arrLength):
            # Insert windowSum to curr index
            decodedArr[i] = windowSum

            # slide window
            windowSum -= code[(start + i) % arrLength] # drop outgoing element
            windowSum += code[(end + i + 1) % arrLength] # add incoming element
        
        return decodedArr
        

        
    
sol = Solution()
first_dec = sol.decrypt([5,7,1,4], 3)
print(first_dec)
sec_dec = sol.decrypt([2,4,9,3], -2)
print(sec_dec)
# third_dec = sol.decrypt([10,5,7,7,3,2,10,3,6,9,1,6], -4)
# print(third_dec)
