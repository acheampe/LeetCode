import unittest

class Solution:
    def alienOrder(self, words: list[str]) -> str:
        
        chr_graph: dict[str, set[str]] = {c: set() for word in words for c in word}
        
        for i in range(len(words) - 1):
            first_word, second_word = words[i], words[i + 1]
            min_length = min(len(first_word), len(second_word))
            
            for i in range(min_length):
                if first_word[i] != second_word[i]:
                    chr_graph[first_word[i]].add(second_word[i])
                    break
                
                elif len(second_word) < len(first_word):
                    return "" # not lexi ordered
            
        result = []
        completed_path = set()
        
        def isCycle(c, curr_path):
            
            if c in curr_path:
                return True # it is a cycle
            
            if c in completed_path:
                return False # it is not a cycle
            
            curr_path.add(c)
            
            for next_c in chr_graph[c]:
                cycle_detected = isCycle(next_c, curr_path) 
                if cycle_detected:
                    return True
            
            # post DFS
            completed_path.add(c)
            result.append(c)
            
            return False
        
        for chr in chr_graph.keys():
            if chr in completed_path:
                continue
                
            curr_path = set()
            if isCycle(chr, curr_path):
                return ""
        
        return ''.join(l for l in result[::-1])


class TestAlienDictionary(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def isValidOrder(self, order: str, words: list[str]) -> bool:
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