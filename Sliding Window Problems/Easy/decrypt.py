from typing import List
## 1652. Defuse the Bomb

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        """
        Decrypts current window and places decrypted value in previous index
        """

        # Edge case
        if k > len(code):
            print("Invalid")
            return -1 
        
        # initialize decryptArr to 0s
        decryptCode = [ 0 for i in range(len(code))]

        # Calc. first window and initialize to previous index
        currSum = sum(code[:k])

        # Set up a wrap around loop
        for i in range(len(code)):
            if i == 0:
                decryptCode[len(code) - 1] = currSum
            
            else:
                # subtracting init window index and adding last window index
                currSum = currSum - (code[(i - 1) % len(code)]) + (code[(k + i - 1) % len(code)])
                decryptCode[i - 1] = currSum
        
        return decryptCode
    
sol = Solution()
first_dec = sol.decrypt([5,7,1,4], 3)
print(first_dec)