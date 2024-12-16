from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        function to determine if string is a palindrome
        """

        # Initiate variables
        start = 0 
        end = len(s) - 1
        
        # Establishing termination condition
        while start < end:

            # if start and end chrs ==
            startLetter, endLetter = s[start].lower(), s[end].lower()
            if startLetter == endLetter:
                start += 1
                end -= 1
            
            startLetter, endLetter = s[start].lower(), s[end].lower()
            while start < end and ord(startLetter) < ord('a') or ord(startLetter) > ord('z'):
                start += 1
                startLetter = s[start].lower()


            startLetter, endLetter = s[start].lower(), s[end].lower()
            while end > start and ord(endLetter) < ord('a') or ord(endLetter) > ord('z'):
                end -= 1
                endLetter = s[end].lower()
            
            startLetter, endLetter = s[start].lower(), s[end].lower()
            if startLetter != endLetter:
                return False
        
        return True

sol = Solution()
# print(sol.isPalindrome("A man, a plan, a canal: Panama")) # Expected: true
# print(sol.isPalindrome("race a car")) # Expected: false
# print(sol.isPalindrome(" ")) # Expected: true
print(sol.isPalindrome(".,")) # Expected: true