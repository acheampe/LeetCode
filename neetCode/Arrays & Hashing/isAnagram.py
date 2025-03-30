from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """return boolean if both inputs strings are anagrams"""
        
        # # Questions to Ask Interviewer:
        # # will all inputs be a string? 
        # # If string, are they all lower case?
        # # should I concern myself with empty strings?
        # # Can I manipulate the input string 
        # # Clarify to see if length of each input array will always be the same or not

        if len(s) != len(t):
            return False

        countS = Counter(s) # O(n) TC and SC
        countT = Counter(t) # O(n) TC and SC
        
        for key in countS.keys():
            
            if countS[key] != countT[key]:
                return False # no duplicate found
            
        return True
        ##################
        # SECOND APPROACH #
        # sortS = sorted(s) # O(n log n) TC and O(n) SC
        # sortT = sorted(t) # O(n log n) TC and O(n) SC
        
        # for i in range(len(sortS)): # O(n) TC
        #     if sortS[i] != sortT[i]:
        #         return False
        
        # return True
        ###################
        # if len(s) != len(t):
        #     return False

        # count = [0] * 26  # one slot for each letter in the alphabet

        # for i in range(len(s)):
        #     count[ord(s[i]) - ord('a')] += 1
        #     count[ord(t[i]) - ord('a')] -= 1

        # for val in count:
        #     if val != 0:
        #         return False

        # return True