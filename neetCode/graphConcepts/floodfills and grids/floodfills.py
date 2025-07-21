import unittest

class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:

        currColor = image[sr][sc]
        seen = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] # right, left, down, up respectively for adjacent checks. If diagonals were needed, 4 more coordinates will be integrated

        #check if we need to do floodfill 
        if currColor == color:
            return image # no further changes needed

        def dfs(r, c):
            
            # create base conditions
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]):
                return # invalid coordinates

            if (r, c) in seen:
                return
            
            if image[r][c] != currColor:
                return # no need to proceed further, only wanna change valid fields
            
            seen.add((r,c))
            image[r][c] = color

            for dr, dc in directions:
                dfs(r + dr, c + dc) # SC = O(m * n) for recursive stack and TC = O(m *n) for visiting all cells.
        
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