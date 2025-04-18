import unittest

# class Solution:
#     def numIslands(self, grid: list[list[str]]) -> int:
#         if not grid:
#             return 0

#         m, n = len(grid), len(grid[0])
#         parent = {}
#         count = 0  # number of land cells (each will start as its own island)

#         def get_id(i, j):
#             return i * n + j  # 2D → 1D mapping

#         def find(x):
#             if parent[x] != x:
#                 parent[x] = find(parent[x])  # path compression
#             return parent[x]

#         def union(x, y):
#             root_x = find(x)
#             root_y = find(y)
#             if root_x != root_y:
#                 parent[root_y] = root_x

#         # Step 1: Initialize parent for each land cell
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == '1':
#                     idx = get_id(i, j)
#                     parent[idx] = idx  # initially, parent is itself
#                     count += 1

#         # Step 2: Union adjacent land cells (right, down)
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == '1':
#                     for dx, dy in [(1, 0), (0, 1)]:  # down and right
#                         ni, nj = i + dx, j + dy
#                         if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == '1':
#                             union(get_id(i, j), get_id(ni, nj))

#         # Step 3: Count distinct root parents (only for land)
#         root_set = set()
#         for node in parent:
#             root_set.add(find(node))

#         return len(root_set)
        


class TestNumIslands(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    # def test_single_large_island(self): 
    #     grid = [
    #         ["1","1","1","1","0"],
    #         ["1","1","0","1","0"],
    #         ["1","1","0","0","0"],
    #         ["0","0","0","0","0"]
    #     ]
    #     self.assertEqual(self.sol.numIslands(grid), 1)

    # def test_multiple_small_islands(self):
    #     grid = [
    #         ["1","1","0","0","0"],
    #         ["1","1","0","0","0"],
    #         ["0","0","1","0","0"],
    #         ["0","0","0","1","1"]
    #     ]
    #     self.assertEqual(self.sol.numIslands(grid), 3)

    # def test_single_cell_island(self):
    #     grid = [["1"]]
    #     self.assertEqual(self.sol.numIslands(grid), 1)

    def test_single_cell_water(self):
        grid = [["0"]]
        self.assertEqual(self.sol.numIslands(grid), 0)

    # def test_all_water(self):
    #     grid = [
    #         ["0","0","0"],
    #         ["0","0","0"]
    #     ]
    #     self.assertEqual(self.sol.numIslands(grid), 0)

    # def test_all_land(self):
    #     grid = [
    #         ["1","1"],
    #         ["1","1"]
    #     ]
    #     self.assertEqual(self.sol.numIslands(grid), 1)

    # def test_vertical_islands(self):
    #     grid = [
    #         ["1","0","1","0"],
    #         ["1","0","1","0"],
    #         ["1","0","1","0"]
    #     ]
    #     self.assertEqual(self.sol.numIslands(grid), 2)

    # def test_horizontal_islands(self):
    #     grid = [
    #         ["1","1","1"],
    #         ["0","0","0"],
    #         ["1","1","1"]
    #     ]
    #     self.assertEqual(self.sol.numIslands(grid), 2)

if __name__ == '__main__':
    unittest.main()