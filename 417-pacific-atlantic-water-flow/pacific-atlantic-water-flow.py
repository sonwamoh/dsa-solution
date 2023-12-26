class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n_rows, n_cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, ocean, prevH):

            if (r < 0 or c < 0
                or r >= n_rows or c >= n_cols
                or (r, c) in ocean 
                or heights[r][c] < prevH): 
                return

            ocean.add((r, c))
            dfs(r + 1, c, ocean, heights[r][c])
            dfs(r - 1, c, ocean, heights[r][c])
            dfs(r, c + 1, ocean, heights[r][c])
            dfs(r, c - 1, ocean, heights[r][c])
        
        for r in range(n_rows):
            dfs(r, 0, pac, heights[r][0]) 
            dfs(r, n_cols - 1, atl, heights[r][n_cols - 1])
 
        for c in range(0, n_cols):
            dfs(0, c, pac, heights[0][c]) 
            dfs(n_rows - 1, c, atl, heights[n_rows - 1][c])
        
        res = []
        
        for r in range(n_rows):
            for c in range(n_cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append((r, c))
        return res
