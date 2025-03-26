import unittest

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        """
        Return True if s can be segmented into words in wordDict.
        TC: O(n^2) – due to substring slicing and overlapping subproblems
        SC: O(n) – for memoization table and recursion stack
        """

        wordSet = set(wordDict)
        memo = {}

        def dfs(startIndex):
            if startIndex == len(s):
                return True  # reached end successfully

            if startIndex in memo:
                return memo[startIndex]

            for endIndex in range(startIndex + 1, len(s) + 1):
                word = s[startIndex:endIndex]
                if word in wordSet and dfs(endIndex):
                    memo[startIndex] = True
                    return True

            memo[startIndex] = False
            return False

        return dfs(0)

class TestWordBreak(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        s = "leetcode"
        wordDict = ["leet", "code"]
        self.assertTrue(self.sol.wordBreak(s, wordDict))

    def test_example_2(self):
        s = "applepenapple"
        wordDict = ["apple", "pen"]
        self.assertTrue(self.sol.wordBreak(s, wordDict))

    def test_example_3(self):
        s = "catsandog"
        wordDict = ["cats", "dog", "sand", "and", "cat"]
        self.assertFalse(self.sol.wordBreak(s, wordDict))

    def test_single_character(self):
        s = "a"
        wordDict = ["a"]
        self.assertTrue(self.sol.wordBreak(s, wordDict))

    def test_no_possible_segmentation(self):
        s = "helloworld"
        wordDict = ["hello", "planet"]
        self.assertFalse(self.sol.wordBreak(s, wordDict))

    def test_word_reuse(self):
        s = "aaaaaaa"
        wordDict = ["aaaa", "aaa"]
        self.assertTrue(self.sol.wordBreak(s, wordDict))

if __name__ == "__main__":
    unittest.main()