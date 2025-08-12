import unittest

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        # Fill in your DFS or BFS logic here
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # up, down, left, right
        m, n = len(grid), len(grid[0])
        seen = set()
        count = 0 
        
        def formIsland(x, y):
            
            for dr, dc in directions:
                if x + dr >= 0 and x + dr < m and y + dc >= 0 and y + dc < n:
                    if grid[x + dr][y + dc] == "1" and (x + dr, y + dc) not in seen: # if true then it makes up part of the island  
                        seen.add((( dr + x, dc + y )))
                        formIsland( dr + x, dc + y )

            
        for i in range(m):
            for j in range(n):
                if (i, j) not in seen:
                    seen.add((i, j))
                    count += 1 # count as an island since not in seen
                    formIsland(i, j) # find and add all coordinates to seen that makes the island 
                        
        return count
        


class TestNumIslands(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        grid = [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
        ]
        expected = 1
        self.assertEqual(self.sol.numIslands(grid), expected)

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