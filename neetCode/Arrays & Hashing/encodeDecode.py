import unittest

class Solution:

    def encode(self, strs: list[str]) -> str:
        """TC & SC = O(n)"""
        encoded = ''
        for word in strs:
            currLength = len(word)
            encoded = ''.join(encoded + str(currLength)+ '#' + word)
        
        return encoded

    def decode(self, s: str) -> list[str]:
        """TC and SC = O(n)"""
        
        index = 0
        result = []
        
        isKey = ''
        while index < len(s):
            
            if s[index] != '#':
                isKey = ''.join(isKey + s[index])
                index += 1
            
            elif s[index] == '#':
                isWordLength = int(isKey)
                result.append(s[index + 1 : isWordLength + index + 1])
                
                index = isWordLength + index + 1
                isKey = ''
        
        return result
        

class TestEncodeDecodeStrings(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_example_1(self):
        strs = ["neet", "code", "love", "you"]
        self.assertEqual(self.sol.decode(self.sol.encode(strs)), strs)

    def test_example_2(self):
        strs = ["we", "say", ":", "yes"]
        self.assertEqual(self.sol.decode(self.sol.encode(strs)), strs)

    def test_empty_list(self):
        strs = []
        self.assertEqual(self.sol.decode(self.sol.encode(strs)), strs)

    def test_list_with_empty_string(self):
        strs = [""]
        self.assertEqual(self.sol.decode(self.sol.encode(strs)), strs)

    def test_multiple_empty_strings(self):
        strs = ["", "", ""]
        self.assertEqual(self.sol.decode(self.sol.encode(strs)), strs)

    def test_utf8_characters(self):
        strs = ["こんにちは", "你好", "😊"]
        self.assertEqual(self.sol.decode(self.sol.encode(strs)), strs)

if __name__ == '__main__':
    unittest.main()