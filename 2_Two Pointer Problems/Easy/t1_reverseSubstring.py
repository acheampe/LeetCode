from typing import List

# Time Complexity O(n). Space Complexity O(1).
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        leftPointer, rightPointer = 0, len(s) - 1

        while leftPointer < rightPointer:
            # Swap values
            s[leftPointer], s[rightPointer] = s[rightPointer], s[leftPointer]
            leftPointer += 1
            rightPointer -=1 

sol = Solution()
print(sol.reverseString(["h","e","l","l","o"])) # Expected: ["o","l","l","e","h"]
print(sol.reverseString(["H","a","n","n","a","h"])) # Expected: ["h","a","n","n","a","H"]