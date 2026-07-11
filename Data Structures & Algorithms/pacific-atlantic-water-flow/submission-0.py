class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific_visited = set()
        atlantic_visited = set()

        def dfs(r, c, visit, prevHeight):
            if (r < 0 or c < 0 or r == ROWS or c == COLS or
            (r,c) in visit or heights[r][c] < prevHeight):
                return
            # can be flowed so add to visit
            visit.add((r,c))
            # keep exploring in four directions
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
        
        for c in range(COLS):
            # start from pacific (first row)
            dfs(0, c, pacific_visited, heights[0][c])
            # start from atlantic (last row)
            dfs(ROWS - 1, c, atlantic_visited, heights[ROWS - 1][c])
        
        for r in range(ROWS):
            # start from pacific (first col)
            dfs(r, 0, pacific_visited, heights[r][0])
            # start from atlantic (last col)
            dfs(r, COLS - 1, atlantic_visited, heights[r][COLS - 1])
        
        results = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pacific_visited and (r,c) in atlantic_visited:
                    results.append([r,c])
        return results
