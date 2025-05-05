import unittest

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        """
        TC and SC == O(m*n)
        """
        if not grid:
            return 0

        parent = {}
        m, n = len(grid), len(grid[0]) # row and column

        def find(x):
            """use path compression to lead parent"""
            if parent[x] != x:
                parent[x] = find(parent[x]) # to search for lead parent 
            return parent[x]
        
        def union(x, y):
            """path compress these two connection"""

            x_root = find(x)
            y_root = find(y)

            if x_root != y_root:
                parent[y_root] = x_root
        
        def get_id(r, c):
            return ((r * n) + c) # to create a unique id
        
        # initiate parent id to themself
        for i in range(m):
            for j in range(n):

                if grid[i][j] == '1':
                    # make id
                    idx = get_id(i, j)
                    parent[idx] = idx
        
        # unite connected islands
        for i in range(m):
            for j in range(n):

                if grid[i][j] == '1':
                    for dx, dy in [(1, 0), (0, 1)]: # due to iteration direction we only need to check right and down
                        rx, cy = i + dx, j + dy

                        if (0 <= rx < m) and ( 0 <= cy < n) and grid[rx][cy] == '1': # then unite
                            union(get_id(i, j), get_id(rx, cy))
        
        uniqueParents = set()
        for val in parent.values():
            uniqueParents.add(find(val))

        return len(uniqueParents)
    
# class Solution:
#     def numIslands(self, grid: list[list[str]]) -> int:
#         """return number of islands;
#         Time complexity: O(mn), worst case(O(mn) and space complexity O(n) 
#         worse case for parent
#         """
        
#         if not grid:
#             return 0

#         parent = {} # 1D key to track 2D iteration

#         m, n = len(grid), len(grid[0])

#         def get_id(r, c):
#             return r * n + c # 2d -> 1d mapping
        
#         #used to find parent
#         def find(isle):
#             """find parent"""
#             if parent[isle] != isle:
#                 parent[isle] = find(parent[isle])
#             return parent[isle]
        
#         def union(node1, node2):
#             """unit nodes through path compression"""
            
#             root1, root2 = find(node1), find(node2)
            
#             if root1 != root2:
#                 parent[root2] = root1 
        
#         # Initiate parent
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == '1':
#                     idx = get_id(i, j)
#                     parent[idx] = idx

#         # Unionize adjacent grids
#         for i in range(m):
#             for j in range(n):

#                 if grid[i][j] == '1':
#                     # Union set grid to cover only right and down direction
#                     for dx, dy in [(1, 0), (0, 1)]:
#                         mr, nc = dx + i, dy + j

#                         if (0 <= mr < m) and (0 <= nc < n) and grid[mr][nc] == '1':
#                             union(get_id(i, j), get_id(mr, nc))
                    
#         distinctIsle = set()
        
#         for node in parent:
#             distinctIsle.add(find(node))
        
#         return len(distinctIsle)


class TestNumIslands(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_single_large_island(self): 
        grid = [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
        ]
        self.assertEqual(self.sol.numIslands(grid), 1)

    def test_multiple_small_islands(self):
        grid = [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ]
        self.assertEqual(self.sol.numIslands(grid), 3)

    def test_single_cell_island(self):
        grid = [["1"]]
        self.assertEqual(self.sol.numIslands(grid), 1)

    def test_single_cell_water(self):
        grid = [["0"]]
        self.assertEqual(self.sol.numIslands(grid), 0)

    def test_all_water(self):
        grid = [
            ["0","0","0"],
            ["0","0","0"]
        ]
        self.assertEqual(self.sol.numIslands(grid), 0)

    def test_all_land(self):
        grid = [
            ["1","1"],
            ["1","1"]
        ]
        self.assertEqual(self.sol.numIslands(grid), 1)

    def test_vertical_islands(self):
        grid = [
            ["1","0","1","0"],
            ["1","0","1","0"],
            ["1","0","1","0"]
        ]
        self.assertEqual(self.sol.numIslands(grid), 2)

    def test_horizontal_islands(self):
        grid = [
            ["1","1","1"],
            ["0","0","0"],
            ["1","1","1"]
        ]
        self.assertEqual(self.sol.numIslands(grid), 2)

if __name__ == '__main__':
    unittest.main()