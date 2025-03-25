import unittest

# Assume this is the solution stub you provided
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        pass

class TestSearchInRotatedSortedArray(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        self.assertEqual(self.sol.search([4,5,6,7,0,1,2], 0), 4)

    def test_example_2(self):
        self.assertEqual(self.sol.search([4,5,6,7,0,1,2], 3), -1)

    def test_example_3(self):
        self.assertEqual(self.sol.search([1], 0), -1)

    def test_not_rotated(self):
        self.assertEqual(self.sol.search([1, 2, 3, 4, 5], 3), 2)

    def test_rotated_at_middle(self):
        self.assertEqual(self.sol.search([6,7,8,1,2,3,4,5], 2), 4)

    def test_single_element_found(self):
        self.assertEqual(self.sol.search([10], 10), 0)

    def test_large_array_target_absent(self):
        nums = list(range(1000, 10000)) + list(range(1, 999))
        self.assertEqual(self.sol.search(nums, -1), -1)

    def test_large_array_target_present(self):
        nums = list(range(1000, 10000)) + list(range(1, 999))
        self.assertEqual(self.sol.search(nums, 1234), nums.index(1234))

if __name__ == "__main__":
    unittest.main()