import unittest

class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        
        currentColor = image[sr][sc]
        
        if currentColor == color:
            return image
        
        seen = set()
        
        def dfs(r, c):
            # base case: out of bounds
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]):
                return
            
            # already visited
            if (r, c) in seen:
                return
            
            # not the same color → don't flood
            if image[r][c] != currentColor:
                return

            # mark visited
            seen.add((r, c))

            # flood fill current
            image[r][c] = color

            # explore neighbors
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
                
        dfs(sr, sc)
        
        return image


class TestFloodFill(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    # def test_example1(self):
    #     image = [[1,1,1],[1,1,0],[1,0,1]]
    #     sr = 1
    #     sc = 1
    #     color = 2
    #     expected = [[2,2,2],[2,2,0],[2,0,1]]
    #     self.assertEqual(self.sol.floodFill(image, sr, sc, color), expected)

    # def test_example2(self):
    #     image = [[0,0,0],[0,0,0]]
    #     sr = 0
    #     sc = 0
    #     color = 0
    #     expected = [[0,0,0],[0,0,0]]
    #     self.assertEqual(self.sol.floodFill(image, sr, sc, color), expected)

    # def test_no_neighbors(self):
    #     image = [[0,1,0],[1,1,1],[0,1,0]]
    #     sr = 0
    #     sc = 0
    #     color = 9
    #     expected = [[9,1,0],[1,1,1],[0,1,0]]
    #     self.assertEqual(self.sol.floodFill(image, sr, sc, color), expected)

    # def test_all_same(self):
    #     image = [[1,1],[1,1]]
    #     sr = 0
    #     sc = 0
    #     color = 3
    #     expected = [[3,3],[3,3]]
    #     self.assertEqual(self.sol.floodFill(image, sr, sc, color), expected)

    # def test_diagonal_no_fill(self):
    #     image = [[1,0,1],
    #              [0,1,0],
    #              [1,0,1]]
    #     sr = 1
    #     sc = 1
    #     color = 5
    #     expected = [[1,0,1],
    #                 [0,5,0],
    #                 [1,0,1]]
    #     self.assertEqual(self.sol.floodFill(image, sr, sc, color), expected)
        
    def test_all_same2(self):
        image = [[0,0,0],[0,0,0]]
        sr = 0
        sc = 0
        color = 2
        expected = [[2,2,2],[2,2,2]]
        self.assertEqual(self.sol.floodFill(image, sr, sc, color), expected)

if __name__ == '__main__':
    unittest.main()