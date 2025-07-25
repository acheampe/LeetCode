import unittest

from collections import deque 

class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:

        if image[sr][sc] == color:
            return image
        
        isColor = image[sr][sc]

        directions = [(-1, 0), (1, 0), (0,1), (0, -1)] # up, down, left, right respectively

        stack = deque()

        stack.append((sr, sc))

        while stack:
            r, c = stack.popleft()
            image[r][c] = color

            for dr, dc in directions:
                sumRow, sumCol = dr + r, dc + c
                if (0 <= sumRow < len(image)) and (0 <= sumCol < len(image[0])) and image[sumRow][sumCol] == isColor:
                    stack.append((sumRow, sumCol))
        
        return image
        
       


class TestFloodFill(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        image = [[1,1,1],[1,1,0],[1,0,1]]
        sr = 1
        sc = 1
        color = 2
        expected = [[2,2,2],[2,2,0],[2,0,1]]
        self.assertEqual(self.sol.floodFill(image, sr, sc, color), expected)

    def test_example2(self):
        image = [[0,0,0],[0,0,0]]
        sr = 0
        sc = 0
        color = 0
        expected = [[0,0,0],[0,0,0]]
        self.assertEqual(self.sol.floodFill(image, sr, sc, color), expected)

    def test_no_neighbors(self):
        image = [[0,1,0],[1,1,1],[0,1,0]]
        sr = 0
        sc = 0
        color = 9
        expected = [[9,1,0],[1,1,1],[0,1,0]]
        self.assertEqual(self.sol.floodFill(image, sr, sc, color), expected)

    def test_all_same(self):
        image = [[1,1],[1,1]]
        sr = 0
        sc = 0
        color = 3
        expected = [[3,3],[3,3]]
        self.assertEqual(self.sol.floodFill(image, sr, sc, color), expected)

    def test_diagonal_no_fill(self):
        image = [[1,0,1],
                 [0,1,0],
                 [1,0,1]]
        sr = 1
        sc = 1
        color = 5
        expected = [[1,0,1],
                    [0,5,0],
                    [1,0,1]]
        self.assertEqual(self.sol.floodFill(image, sr, sc, color), expected)
        
    def test_all_same2(self):
        image = [[0,0,0],[0,0,0]]
        sr = 0
        sc = 0
        color = 2
        expected = [[2,2,2],[2,2,2]]
        self.assertEqual(self.sol.floodFill(image, sr, sc, color), expected)

if __name__ == '__main__':
    unittest.main()