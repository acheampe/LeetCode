from typing import List
## 1652. Defuse the Bomb

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        """
        To determine the sum of curr window size k and place in respective
        index determine by pos/neg k val
        """

        # Establish variables
        arrlen = len(code) # length of array
        absK = abs(k) # ensure positive val of k when needed
        decryptCode = [0 for i in range(arrlen)] # initialize newArr with 0s
        currSum = sum(code[:absK]) # absolute k here

        for i in range(arrlen):

            # Address neg k condition
            if k < 0:   # we want k, not absK to determine neg or pos val
                if i == 0:
                    decryptCode[absK] = currSum
            
                else:
                    currSum = currSum - code[(i  - 1) % arrlen] + code[(absK + i - 1) % arrlen]
                    decryptCode[(absK + i )% arrlen] = currSum
            
            # Address pos k condition
            if k > 0:
                if i == 0:
                    decryptCode[arrlen - 1] = currSum
                
                else:
                    currSum = currSum - code[(i - 1) % arrlen] + code[(k + i - 1) % arrlen]
                    decryptCode[(i - 1) % arrlen] = currSum
            
        return decryptCode 
        

        
    
sol = Solution()
# first_dec = sol.decrypt([5,7,1,4], 3)
# print(first_dec)
sec_dec = sol.decrypt([2,4,9,3], -2)
print(sec_dec)
# third_dec = sol.decrypt([10,5,7,7,3,2,10,3,6,9,1,6], -4)
# print(third_dec)
