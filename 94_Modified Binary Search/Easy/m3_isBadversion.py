import unittest
from typing import List

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n  # Ensure left starts from 1 (since versions are 1-based)

        while left < right:
            mid = left + (right - left) // 2

            if isBadVersion(mid):  # mid could be the first bad version
                right = mid  # Move leftward
            else:
                left = mid + 1  # Move rightward

        return left  # The first bad version
    
    def summaryApproach(self):
        """
        Though this problem is very simple and by all means ranked, Leetcode
        easy, it is important to not lose foresight on what the problem want you 
        to return

        First, the bruteforce approach will be to iterate through the range thill
        we encounter the first value that isBadversion. This is an O(n) approach.
        We do run the risk of TLE if we are parsing through a very large input.

        The optimize approach will be through a binary search, resulting in 
        O(log n) time complexity and O(1) space complexity. 

        To the determine if the problem can be solved as a binary search, it is 
        important to ask if the return value that you seek, can be resursively
        search in just half of the available array and if so, what conditions will
        make it possible. 

        It this problem, we seek to return the first bad value, every other value after 
        is deemed as bad. 

        if the midpoint of the range is bad, it could be our first bad value, 
        so we search the left branch of our current array, inclusive of the midpoint 
        (this is what tripped me up when originally solving this). We make it inclusive 
        because it could be the last midpoint that we are seeking. if it is, it will be 
        our answer to the problem by end of iteration/recursion approach becuase we return left at the end.

        if mid point of the next iterative array is good, we search the right side (mid + 1).
        """
  
import unittest

# Mocking the isBadVersion API
def isBadVersion(version: int) -> bool:
    return version >= bad_version

class TestFirstBadVersion(unittest.TestCase):
    def test_case_1(self):
        global bad_version
        bad_version = 4
        solution = Solution()
        self.assertEqual(solution.firstBadVersion(5), 4)
    
    # def test_case_2(self):
    #     global bad_version
    #     bad_version = 1
    #     solution = Solution()
    #     self.assertEqual(solution.firstBadVersion(1), 1)
    
    # def test_case_3(self):
    #     global bad_version
    #     bad_version = 10
    #     solution = Solution()
    #     self.assertEqual(solution.firstBadVersion(20), 10)
    
    # def test_case_4(self):
    #     global bad_version
    #     bad_version = 100
    #     solution = Solution()
    #     self.assertEqual(solution.firstBadVersion(200), 100)
    
    # def test_case_5(self):
    #     global bad_version
    #     bad_version = 5000
    #     solution = Solution()
    #     self.assertEqual(solution.firstBadVersion(10000), 5000)

if __name__ == "__main__":
    unittest.main()

