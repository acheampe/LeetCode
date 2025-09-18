import unittest

from gridtools.features.max_water_area import max_water_area
from gridtools.connectivity import neighbors_4, neighbors_8


class TestMaxWaterAreaBlackBox(unittest.TestCase):

    def test_all_land_returns_zero(self):
        grid = [
            [0, 0],
            [0, 0],
        ]
        self.assertEqual(
            max_water_area(grid, neighbors_4), 0,
            "All land grid should yield max area 0"
        )
        self.assertEqual(
            max_water_area(grid, neighbors_8), 0,
            "All land grid should yield max area 0"
        )

    def test_single_big_cluster(self):
        grid = [
            [1, 1, 1],
            [1, 1, 1],
        ]
        # One contiguous cluster of size 6
        self.assertEqual(
            max_water_area(grid, neighbors_4), 6,
            "Expected one big cluster area = 6"
        )
        self.assertEqual(
            max_water_area(grid, neighbors_8), 6,
            "Expected one big cluster area = 6"
        )

    def test_multiple_clusters_neighbors_4_vs_8(self):
        grid = [
            [1, 0, 1],
            [0, 1, 0],
            [1, 0, 1],
        ]
        # For 4-neighbors: 5 isolated water cells -> each max = 1
        self.assertEqual(
            max_water_area(grid, neighbors_4), 1,
            "With 4-neighbors, diagonals do not connect"
        )
        # For 8-neighbors: all diagonals connect into one cluster of size 5
        self.assertEqual(
            max_water_area(grid, neighbors_8), 5,
            "With 8-neighbors, diagonals connect into one large region"
        )

    def test_largest_cluster_not_first(self):
        grid = [
            [1, 0, 0, 0],
            [1, 0, 1, 1],
            [0, 0, 1, 1],
        ]
        # Cluster A: (0,0)-(1,0) = size 2
        # Cluster B: bottom-right square of 4 cells = size 4
        self.assertEqual(
            max_water_area(grid, neighbors_4), 4,
            "Should return largest cluster size (4) not first cluster (2)"
        )
        self.assertEqual(
            max_water_area(grid, neighbors_8), 4,
            "Even with diagonals, cluster B remains size 4"
        )

    def test_irregular_shape(self):
        grid = [
            [0, 1, 1, 0],
            [1, 1, 0, 0],
            [0, 1, 1, 1],
        ]
        # For 4-neighbors: all but one connect = region of size 7
        self.assertEqual(
            max_water_area(grid, neighbors_4), 7,
            "Expected max cluster size 7 using 4-neighbors"
        )
        # For 8-neighbors: diagonals tie everything together = size 8
        self.assertEqual(
            max_water_area(grid, neighbors_8), 7,
            "Expected max cluster size 7 using 8-neighbors"
        )

    def test_empty_grid_return_zero(self):
        grid = []

        self.assertEqual(max_water_area(grid, neighbors_4),
                            0,
                            msg = f"expected 0 since grid is empty"
                            )

        self.assertEqual(max_water_area(grid, neighbors_8),
                            0,
                            msg = f"expected 0 since grid is empty"
                            ) 
