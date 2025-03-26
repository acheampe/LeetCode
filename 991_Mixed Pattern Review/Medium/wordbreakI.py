import unittest


# Assume the solution stub exists
class Solution:
        def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        pass

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