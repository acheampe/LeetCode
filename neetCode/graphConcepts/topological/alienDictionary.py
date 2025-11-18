import unittest
from typing import List

class Solution:
    def alienOrder(self, words: list[str]) -> str:
        # <-- Implement this part
        pass


class TestAlienDictionary(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def isValidOrder(self, order: str, words: List[str]) -> bool:
        """Check if the given order is valid for the word list"""
        rank = {c: i for i, c in enumerate(order)}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if rank[c1] > rank[c2]:
                        return False
                    break
            else:
                # If no diff and w2 is prefix of w1, it's invalid
                if len(w2) < len(w1):
                    return False
        return True

    def test_example_1(self):
        words = ["wrt", "wrf", "er", "ett", "rftt"]
        result = self.sol.alienOrder(words)
        self.assertTrue(self.isValidOrder(result, words))

    def test_example_2(self):
        words = ["z", "x"]
        result = self.sol.alienOrder(words)
        self.assertTrue(self.isValidOrder(result, words))

    def test_example_3(self):
        words = ["z", "x", "z"]
        result = self.sol.alienOrder(words)
        self.assertEqual(result, "")  # cycle, no valid order

    def test_single_word(self):
        words = ["abc"]
        result = self.sol.alienOrder(words)
        self.assertTrue(set(result).issuperset(set("abc")))

    def test_same_words(self):
        words = ["abc", "abc"]
        result = self.sol.alienOrder(words)
        self.assertTrue(set(result).issuperset(set("abc")))

if __name__ == "__main__":
    unittest.main()