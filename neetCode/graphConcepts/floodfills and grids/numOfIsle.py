import unittest

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        # Fill in your DFS or BFS logic here
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # up, down, left, right
        m, n = len(grid), len(grid[0])
        seen = set()
        count = 0 
        
        def isIsland(x, y):
            
            # base cases
            if  x < 0 or x >= m or y < 0 or y >= n:
                return True # out of bounds are assumed to be zeros, and all coords need to be 0 to quantify adj surroundings as an Island

            
            if (x, y) not in seen:
                for dr, dc in directions:
                    while not grid[x][y] == "1" and isIsland( dr + x, dc + y ):
                        seen.add((( dr + x, dc + y )))
                        return False
                    seen.add((( dr + x, dc + y )))
            seen.add((x, y))
            return True

            
        for i in range(m):
            for j in range(n):
                if (i, j) not in seen:
                    if isIsland(i, j): # returns true if coord and it's adj forms a valid island
                        count += 1
        return count
        


class TestNumIslands(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    # def test_example1(self):
    #     grid = [
    #         ["1","1","1","1","0"],
    #         ["1","1","0","1","0"],
    #         ["1","1","0","0","0"],
    #         ["0","0","0","0","0"]
    #     ]
    #     expected = 1
    #     self.assertEqual(self.sol.numIslands(grid), expected)

    # def test_example2(self):
    #     grid = [
    #         ["1","1","0","0","0"],
    #         ["1","1","0","0","0"],
    #         ["0","0","1","0","0"],
    #         ["0","0","0","1","1"]
    #     ]
    #     expected = 3
    #     self.assertEqual(self.sol.numIslands(grid), expected)

    # def test_single_land_cell(self):
    #     grid = [["1"]]
    #     expected = 1
    #     self.assertEqual(self.sol.numIslands(grid), expected)

    # def test_single_water_cell(self):
    #     grid = [["0"]]
    #     expected = 0
    #     self.assertEqual(self.sol.numIslands(grid), expected)

    def test_all_land(self):
        grid = [["1","1"],["1","1"]]
        expected = 1
        self.assertEqual(self.sol.numIslands(grid), expected)

    # def test_checkerboard(self):
    #     grid = [["1","0","1"],
    #             ["0","1","0"],
    #             ["1","0","1"]]
    #     expected = 5
    #     self.assertEqual(self.sol.numIslands(grid), expected)

if __name__ == '__main__':
    unittest.main()