import unittest 
# class Solution:
#     def rob(self, nums: list[int]) -> int:
#         """
#         return max value without triggering an alarm
#         TC: O(n)
#         SC: O(1)
#         """
        
#         prev, curr = 0, 0
        
#         # [prev, curr, n, n + 1, n + 2,...]
#         for num in nums:
#             total = max(num + prev, curr)
#             prev = curr
#             curr = total
                    
#         return curr

class Solution:
    def rob(self, nums: list[int]) -> int:
        """
        Recursive solution with memoization (Top-Down DP)
        TC: O(n)
        SC: O(n) for memoization and recursion stack
        """
        memo = {}

        def dfs(index):
            if index >= len(nums):
                return 0

            if index in memo:
                return memo[index]

            # Option 1: Rob current house and move to index + 2
            # Option 2: Skip current house and move to index + 1
            memo[index] = max(nums[index] + dfs(index + 2), dfs(index + 1))
            return memo[index]

        return dfs(0)

class TestHouseRobber(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        self.assertEqual(self.sol.rob([1, 2, 3, 1]), 4)

    def test_example_2(self):
        self.assertEqual(self.sol.rob([2, 7, 9, 3, 1]), 12)

    def test_single_house(self):
        self.assertEqual(self.sol.rob([10]), 10)

    def test_two_houses(self):
        self.assertEqual(self.sol.rob([10, 20]), 20)

    def test_alternate_max(self):
        self.assertEqual(self.sol.rob([5, 1, 1, 5]), 10)

    def test_all_zeros(self):
        self.assertEqual(self.sol.rob([0, 0, 0, 0]), 0)

    def test_large_values(self):
        self.assertEqual(self.sol.rob([400, 1, 400, 1, 400]), 1200)

if __name__ == "__main__":
    unittest.main()