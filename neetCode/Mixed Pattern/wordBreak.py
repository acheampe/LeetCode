import unittest

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        """return bool if s can be segmented into words in wordDict
        TC and SC == O(n)        
        """
        
        wordDict: set = set(wordDict) # O(n)
        memo = {}
        
        def depthSearch(index):
            
            if index == len(s):
                return True
            
            if index in memo:
                return memo[index]
            
            for i in range(index, len(s)):
                currWord = s[index:i + 1]
                
                if currWord in wordDict and depthSearch(i + 1):
                    memo[index] = True
                    return True
            
            memo[index] = False
            return False
             
        return depthSearch(0)

# class Solution:
#     def wordBreak(self, s: str, wordDict: list[str]) -> bool:
#         wordSet = set(wordDict)
#         n = len(s)
#         dp = [False] * (n + 1)
#         dp[0] = True  # base case: empty string is breakable

#         for i in range(1, n + 1):
#             for j in range(i):
#                 # If s[j:i] is in dict and s[:j] is breakable
#                 if dp[j] and s[j:i] in wordSet:
#                     dp[i] = True
#                     break  # no need to check more j's

#         return dp[n]
####
        


class TestWordBreak(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    # def test_example_1(self):
    #     s = "leetcode"
    #     wordDict = ["leet", "code"]
    #     self.assertTrue(self.sol.wordBreak(s, wordDict))

    # def test_example_2(self):
    #     s = "applepenapple"
    #     wordDict = ["apple", "pen"]
    #     self.assertTrue(self.sol.wordBreak(s, wordDict))

    def test_example_3(self):
        s = "catsandog"
        wordDict = ["cats", "dog", "sand", "and", "cat"]
        self.assertFalse(self.sol.wordBreak(s, wordDict))

    # def test_repeating_word(self):
    #     s = "aaaaaaa"
    #     wordDict = ["aaaa", "aaa"]
    #     self.assertTrue(self.sol.wordBreak(s, wordDict))

    # def test_no_valid_segment(self):
    #     s = "abcd"
    #     wordDict = ["a", "abc", "b", "cd"]
    #     self.assertFalse(self.sol.wordBreak(s, wordDict))

    # def test_single_character_reuse(self):
    #     s = "aaaaaa"
    #     wordDict = ["a"]
    #     self.assertTrue(self.sol.wordBreak(s, wordDict))

    # def test_long_word_dict(self):
    #     s = "pineapplepenapple"
    #     wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
    #     self.assertTrue(self.sol.wordBreak(s, wordDict))

    # def test_exact_match(self):
    #     s = "cat"
    #     wordDict = ["cat"]
    #     self.assertTrue(self.sol.wordBreak(s, wordDict))

if __name__ == '__main__':
    unittest.main()