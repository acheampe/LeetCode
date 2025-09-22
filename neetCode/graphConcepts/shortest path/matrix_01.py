# Leetcode 542
import unittest

class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        pass


class TestUpdateMatrix(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        mat = [[0,0,0],[0,1,0],[0,0,0]]
        expected = [[0,0,0],[0,1,0],[0,0,0]]
        self.assertEqual(
            self.sol.updateMatrix(mat), expected,
            msg=f"Expected {expected}, but got {self.sol.updateMatrix(mat)}"
        )

    def test_example2(self):
        mat = [[0,0,0],[0,1,0],[1,1,1]]
        expected = [[0,0,0],[0,1,0],[1,2,1]]
        self.assertEqual(
            self.sol.updateMatrix(mat), expected,
            msg=f"Expected {expected}, but got {self.sol.updateMatrix(mat)}"
        )

    def test_single_zero(self):
        mat = [[0]]
        expected = [[0]]
        self.assertEqual(self.sol.updateMatrix(mat), expected)

    def test_single_one(self):
        mat = [[1,0]]
        expected = [[1,0]]
        self.assertEqual(self.sol.updateMatrix(mat), expected)

    def test_all_ones_with_one_zero_corner(self):
        mat = [
            [1,1,1],
            [1,1,1],
            [0,1,1]
        ]
        expected = [
            [2,3,4],
            [1,2,3],
            [0,1,2]
        ]
        self.assertEqual(self.sol.updateMatrix(mat), expected)


if __name__ == "__main__":
    unittest.main()