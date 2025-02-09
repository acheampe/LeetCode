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

