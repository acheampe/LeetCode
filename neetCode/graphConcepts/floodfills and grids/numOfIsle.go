package main

func numIslands(grid [][]byte) int {
	var count, m, n int
	mapped := make(map[[2]int]bool)

	if len(grid) > 0 {
		m = len(grid)
		n = len(grid[0])
	}

	directions := [][2]int{
		{0, 1},
		{0, -1},
		{1, 0},
		{-1, 0},
	}

	var mapIsland func(r, c int)
	mapIsland = func(r, c int) {

		if r < 0 || r >= m || c < 0 || c >= n || grid[r][c] == '0' {
			return
		}

		if _, visited := mapped[[2]int{r, c}]; visited {
			return
		}

		mapped[[2]int{r, c}] = true
		for _, d := range directions {
			dr, dc := r+d[0], c+d[1]
			mapIsland(dr, dc)
		}

	}

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if _, visited := mapped[[2]int{i, j}]; !visited && grid[i][j] == '1' {
				count++
				mapIsland(i, j)
			}
		}
	}

	return count
}
