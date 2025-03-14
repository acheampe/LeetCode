import unittest
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        pass

class TestSolution(unittest.TestCase):
    def test_wordBreak(self):
        sol = Solution()
        
        # Basic test cases
        self.assertCountEqual(sol.wordBreak("catsanddog", ["cat","cats","and","sand","dog"]), 
                              ["cats and dog", "cat sand dog"])
        self.assertCountEqual(sol.wordBreak("pineapplepenapple", ["apple","pen","applepen","pine","pineapple"]), 
                              ["pine apple pen apple","pineapple pen apple","pine applepen apple"])
        self.assertCountEqual(sol.wordBreak("catsandog", ["cats","dog","sand","and","cat"]), 
                              [])

        # Edge cases
        self.assertCountEqual(sol.wordBreak("", ["cat","dog"]), [])  # Empty string case
        self.assertCountEqual(sol.wordBreak("a", ["a"]), ["a"])  # Single character match
        self.assertCountEqual(sol.wordBreak("abcd", ["a","abc","b","cd"]), ["a b cd", "abc d"])  # Multiple valid sentences

        # Large input case
        self.assertCountEqual(sol.wordBreak("aaaaaaaaaaaaaaaaaaaa", ["a","aa","aaa","aaaa","aaaaa"]), [])  # No valid full match
        
if __name__ == "__main__":
    unittest.main()        