class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        Will use bfs to determine the entire island
        Whenever bfs function is called, that's when we increment the island count
        Visted set will be used keep track on already visited islands, and we
        ll skip already visited island
        TC: O(m * n) 
        SC: O(m * n) 
        """
        m, n = len(grid), len(grid[0])
        visited = set()
        num_island = 0

        def bfs(r, c):
            queue = [(r,c)]
            visited.add((r,c))
            while queue:
                node = queue.pop(0)
                print(node)
                for x, y in [[0,1], [1,0], [-1,0], [0,-1]]:
                    curr_x, curr_y = node[0] + x, node[1] + y
                    if 0 <= curr_x < m and 0 <= curr_y < n and grid[curr_x][curr_y] == '1' and (curr_x, curr_y) not in visited:
                        queue.append((curr_x, curr_y))
                        visited.add((curr_x, curr_y))

        for i in range(m):
            for j in range(n):
                if  grid[i][j] == "1" and (i, j) not in visited:  
                    bfs(i , j)
                    num_island += 1
        return num_island



        