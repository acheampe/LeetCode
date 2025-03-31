import unittest

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """
        group the anagrams together
        TC: O(n * k)
        SC: O(n)
        """

        # Questions:
        # should i expect edge cases like an empty list/empty string/tow empty strings in list?
        # can input be manipulated directly?
        # will letters be upper and lower case?
        
        groupAnagrams = {} # O(n)
        
        for string in strs:
        
            stringKey = [0] * 26 # O(n) 
            for letter in string:
                stringKey[ord(letter) - ord('a')] += 1
            
            if tuple(stringKey) not in groupAnagrams:
                groupAnagrams[tuple(stringKey)] = [string]
            
            else:
                groupAnagrams[tuple(stringKey)].append(string) 
        
        return [arr for arr in groupAnagrams.values()]

class TestGroupAnagrams(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        output = self.solution.groupAnagrams(strs)
        expected_groups = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

        # Convert each group to a frozenset to ignore ordering within groups
        output_sets = [frozenset(group) for group in output]
        expected_sets = [frozenset(group) for group in expected_groups]
        self.assertCountEqual(output_sets, expected_sets)

    def test_example_2(self):
        strs = [""]
        output = self.solution.groupAnagrams(strs)
        expected = [[""]]
        self.assertEqual(output, expected)

    def test_example_3(self):
        strs = ["a"]
        output = self.solution.groupAnagrams(strs)
        expected = [["a"]]
        self.assertEqual(output, expected)

    def test_all_unique(self):
        strs = ["abc", "def", "ghi"]
        output = self.solution.groupAnagrams(strs)
        expected = [["abc"], ["def"], ["ghi"]]
        output_sets = [frozenset(group) for group in output]
        expected_sets = [frozenset(group) for group in expected]
        self.assertCountEqual(output_sets, expected_sets)

    def test_all_same(self):
        strs = ["abc", "cab", "bca", "cba"]
        output = self.solution.groupAnagrams(strs)
        expected = [["abc", "cab", "bca", "cba"]]
        output_sets = [frozenset(group) for group in output]
        expected_sets = [frozenset(group) for group in expected]
        self.assertCountEqual(output_sets, expected_sets)


if __name__ == '__main__':
    unittest.main()