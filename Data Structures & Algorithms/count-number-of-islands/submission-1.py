class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nrows = len(grid)
        ncols = len(grid[0])
        # define 4 directions
        directions = [(1,0), (-1,0), (0,1), (0, -1)] 
        numIslands = 0

        def dfs(i, j):
            grid[i][j] = "0"
            for di, dj in directions:
                new_i, new_j = i + di, j + dj
                if new_i > -1 and new_i < nrows and new_j > -1 and new_j < ncols and grid[new_i][new_j] == "1":
                    dfs(new_i, new_j)
        
        for i in range(nrows):
            for j in range(ncols):
                if grid[i][j] == "1":
                    dfs(i, j)
                    numIslands += 1

        return numIslands