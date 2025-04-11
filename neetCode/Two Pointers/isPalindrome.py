class Solution:
    def isPalindrome(self, s: str) -> bool:
        """return True if s is a palindrome after 
        removing alphanumeric chrs in string"""
        
        def clarifyingQuestions():
            """
            How do handle empty strings? by definition I can return True
            Should input data be manipulated directly or is it preferred to 
            not manipulate input data (if not I can copy the into data but at a 
            cost of memory)
            """
            pass
        
        def approachDiscussion():
            """
            The first approach I am thinking of taking is to string the string 
            of all non-alphanum chrs, then I can use a two pointer, one on each 
            end to iterate to the middle to see if string is a palindrome. 
            This will cause me to iterate through string twice (each O(n)) and with
            a space complexity of O(n)
            
            I think I can do it in one pass with a SC of O(1) if I carefully place conditionals 
            to ignore non-alphanum...ok I will attempt this approach
            """
            pass
        
        if not s:
            return True
        
        leftPointer, rightPointer = 0, len(s) - 1
        
        while rightPointer > leftPointer:
            
            if s[rightPointer].isalnum() and s[leftPointer].isalnum():
                
                if s[leftPointer].lower() != s[rightPointer].lower():
                    return False
                
                leftPointer += 1
                rightPointer -= 1
            
            elif not s[rightPointer].isalnum():
                rightPointer -= 1
            
            else:
                leftPointer += 1
        
        return True
                      

import unittest

class TestValidPalindrome(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()  # Replace with your class name if different

    # def test_example_1(self):
    #     s = "A man, a plan, a canal: Panama"
    #     self.assertTrue(self.sol.isPalindrome(s))

    # def test_example_2(self):
    #     s = "race a car"
    #     self.assertFalse(self.sol.isPalindrome(s))

    # def test_example_3(self):
    #     s = " "
    #     self.assertTrue(self.sol.isPalindrome(s))

    # def test_single_character(self):
    #     s = "z"
    #     self.assertTrue(self.sol.isPalindrome(s))

    # def test_numbers_and_letters(self):
    #     s = "1a2a1"
    #     self.assertTrue(self.sol.isPalindrome(s))

    # def test_mixed_case(self):
    #     s = "No 'x' in Nixon"
    #     self.assertTrue(self.sol.isPalindrome(s))

    # def test_non_alphanumeric(self):
    #     s = ".,"
    #     self.assertTrue(self.sol.isPalindrome(s))

    # def test_not_palindrome(self):
    #     s = "hello"
    #     self.assertFalse(self.sol.isPalindrome(s))
        
    # def test_large_non_palindrome(self):
    #     s = "A" * 10**5 + "B" + "A" * 10**5
    #     self.assertTrue(self.sol.isPalindrome(s))

    def test_large_palindrome(self):
        s = "A" * 100_000 + "a" + "A" * 100_000
        self.assertTrue(self.sol.isPalindrome(s))
        
    def test_large_non_palindrome(self):
        # Force asymmetry
        s = "A" * 100_000 + "B" + "C" + "A" * 99_999  # Left: 100k A, Right: 99,999 A after "CB"
        self.assertFalse(self.sol.isPalindrome(s))
if __name__ == '__main__':
    unittest.main()
