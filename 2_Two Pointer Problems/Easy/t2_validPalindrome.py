from typing import List

# Time Complexity O(n). Space Complexity O(1).
class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        function to determine if string is a palindrome
        """

        # Initiate two pointer variables
        start, end = 0, len(s) - 1

        while start < end:
            startLetter, endLetter = s[start].lower(), s[end].lower()

            while start < end and not startLetter.isalnum():
                start += 1
                startLetter = s[start].lower()
            
            while end > start and not endLetter.isalnum():
                end -= 1
                endLetter = s[end].lower()
            
            if startLetter != endLetter:
                return False
            
            else:
                start += 1
                end -= 1
        
        return True

    
sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama")) # Expected: true
print(sol.isPalindrome("race a car")) # Expected: false
print(sol.isPalindrome(" ")) # Expected: true
print(sol.isPalindrome(".,")) # Expected: true
print(sol.isPalindrome("0P")) # Expected: false