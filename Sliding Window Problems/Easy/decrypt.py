from typing import List
## 1652. Defuse the Bomb

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        """
        Decrypt current window and places decrypted value in previous index
        """

        arrlen = len(code)
        # initialize decryptArr
        decryptCode = [ 0 for i in range(arrlen)]

        # Calc. first window size
        currSum = sum(code[:k])

        # Set up wrap around loop
        for i in range(arrlen):

            if k < 0: # if neg
                if i == 0:
                    decryptCode[abs(k)] = currSum
                else:
                    currSum = currSum - code[(i - 1) % arrlen] + code[(i + 1) % arrlen]
                    decryptCode[(i + k) % arrlen] = currSum
            
            else:
                if i == 0:
                    decryptCode[arrlen - 1] = currSum
                
                else:
                    # subtracting inti window index and adding last window index from currSum
                    currSum = currSum - code[(i - 1) % arrlen] + code[(k + i - 1) % arrlen]
                    decryptCode[i-1] = currSum
        
        return decryptCode

        
    
sol = Solution()
first_dec = sol.decrypt([5,7,1,4], 3)
print(first_dec)
sec_dec = sol.decrypt([2,4,9,3], -2)
print(sec_dec)