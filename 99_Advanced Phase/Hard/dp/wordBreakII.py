import unittest

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        """
        Return all possible sentences that can be formed from s using words in wordDict.
        Uses recursion + manual memoization.
        
        Time Complexity: O(2^n * n)
        Space Complexity: O(n) (recursion stack + memo storage)
        """
        wordDictSet: set = set(wordDict)  # Convert list to set for O(1) lookups
        memo = {}  # Manually implemented memoization

        def backtrack(i):
            if i in memo:  
                return memo[i]
            
            if i == len(s):
                return [""]  # Base case: Found a valid split

            allSentences = []
            for j in range(i, len(s)):
                word = s[i:j+1]
                if word in wordDictSet:  # Check if valid word
                    rest_sentences = backtrack(j + 1)  # Recursive call
                    for sentence in rest_sentences:
                        allSentences.append(word + (" " + sentence if sentence else ""))  # Construct valid sentence
            
            memo[i] = allSentences 
            return allSentences
        
        return backtrack(0)


class TestSolution(unittest.TestCase):
    def test_wordBreak(self):
        sol = Solution()
        
        # Basic test cases
        self.assertCountEqual(sol.wordBreak("catsanddog", ["cat","cats","and","sand","dog"]), 
                              ["cats and dog", "cat sand dog"])
        # self.assertCountEqual(sol.wordBreak("pineapplepenapple", ["apple","pen","applepen","pine","pineapple"]), 
        #                       ["pine apple pen apple","pineapple pen apple","pine applepen apple"])
        # self.assertCountEqual(sol.wordBreak("catsandog", ["cats","dog","sand","and","cat"]), 
        #                       [])

        # # Edge cases
        # self.assertCountEqual(sol.wordBreak("", ["cat","dog"]), [])  # Empty string case
        # self.assertCountEqual(sol.wordBreak("a", ["a"]), ["a"])  # Single character match
        # self.assertCountEqual(sol.wordBreak("abcd", ["a","abc","b","cd"]), ["a b cd", "abc d"])  # Multiple valid sentences

        # # Large input case
        # self.assertCountEqual(sol.wordBreak("aaaaaaaaaaaaaaaaaaaa", ["a","aa","aaa","aaaa","aaaaa"]), [])  # No valid full match
        
if __name__ == "__main__":
    unittest.main()        
