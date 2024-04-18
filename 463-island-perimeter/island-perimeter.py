class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                square_side = 0
                if grid[i][j] == 1:
                    square_side = 4
                    if i >= 1:
                        if grid[i - 1][j] == 1:
                            square_side -= 1
                    if j >= 1:
                        if grid[i][j - 1] == 1:
                            square_side -= 1
                    if i < len(grid) - 1:
                        if grid[i + 1][j] == 1:
                            square_side -= 1
                    if j < len(grid[0]) - 1:
                        if grid[i][j + 1] == 1:
                            square_side -= 1
                perimeter += square_side
        return perimeter
        