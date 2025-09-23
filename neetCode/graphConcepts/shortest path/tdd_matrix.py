import unittest
from matrix_01 import Solution

class TestupdateMatrix(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()
        
    def test_uniformed_zero_grid(self):
        grid = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]
        
        expected = grid
        returned = self.sol.updateMatrix(grid)
        
        self.assertEqual(expected, returned, msg=f"expected {expected}, returned {returned}")
        
    def test_one_row_grid(self):
        grid = [
            [1, 1, 0],
        ]
        
        expected = [
            [2, 1, 0]
        ]
        returned = self.sol.updateMatrix(grid)
        
        self.assertEqual(expected, returned, msg=f"expected {expected}, returned {returned}")
            

if __name__ == '__main__':
    unittest.main()

#     def test_example1(self):
#         mat = [[0,0,0],[0,1,0],[0,0,0]]
#         expected = [[0,0,0],[0,1,0],[0,0,0]]
#         self.assertEqual(
#             self.sol.updateMatrix(mat), expected,
#             msg=f"Expected {expected}, but got {self.sol.updateMatrix(mat)}"
#         )

#     def test_example2(self):
#         mat = [[0,0,0],[0,1,0],[1,1,1]]
#         expected = [[0,0,0],[0,1,0],[1,2,1]]
#         self.assertEqual(
#             self.sol.updateMatrix(mat), expected,
#             msg=f"Expected {expected}, but got {self.sol.updateMatrix(mat)}"
#         )

#     def test_single_zero(self):
#         mat = [[0]]
#         expected = [[0]]
#         self.assertEqual(self.sol.updateMatrix(mat), expected)

#     def test_single_one(self):
#         mat = [[1,0]]
#         expected = [[1,0]]
#         self.assertEqual(self.sol.updateMatrix(mat), expected)

#     def test_all_ones_with_one_zero_corner(self):
#         mat = [
#             [1,1,1],
#             [1,1,1],
#             [0,1,1]
#         ]
#         expected = [
#             [2,3,4],
#             [1,2,3],
#             [0,1,2]
#         ]
#         self.assertEqual(self.sol.updateMatrix(mat), expected)