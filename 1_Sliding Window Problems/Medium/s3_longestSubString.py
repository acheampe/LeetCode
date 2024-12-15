from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        returns the longest substring without repeating characters
        """

        maxSubString = 0
        leftIndex = 0
        subStringChrs = defaultdict(int)

        # Expansion for loop 
        for rightIndex in range(len(s)):
            subStringChrs[s[rightIndex]] += 1

            # Window reduction condition
            while subStringChrs[s[rightIndex]] > 1:
                subStringChrs[s[leftIndex]] -= 1
                leftIndex += 1
                
            maxSubString = max(maxSubString, rightIndex - leftIndex + 1)
        
        return maxSubString
    
sol = Solution()
print(sol.lengthOfLongestSubstring("pwwkew")) # Expected: 3 
print(sol.lengthOfLongestSubstring("abcabcbb")) # Expected: 3 
print(sol.lengthOfLongestSubstring("bbbbb")) # Expected: 1