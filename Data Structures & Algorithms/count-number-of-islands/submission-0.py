class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        numOfIslands = 0

        def bfs(r, c):
            queue = collections.deque()
            queue.append((r, c))
            # mark visit as visit
            grid[r][c] = "0"

            while queue:
                r, c = queue.popleft()
                # up, down, left, right
                for dr, dc in [(0, 1), (0, -1), (-1, 0), (1,0)]:
                    nr = r + dr
                    nc = c + dc
                    if (nr in range(rows) and
                        nc in range(cols) and
                        grid[nr][nc] == "1"):
                        queue.append((nr,nc))
                        grid[nr][nc] = "0"

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    numOfIslands +=1
                    bfs(r, c)

        return numOfIslands