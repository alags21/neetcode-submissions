class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # iterate through every position in the grid
        # keep track of which things you already explored
        # row = i, col = j
        # position = (i*len(rows) + j)

        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        explored = [[0 for j in range(cols)] for i in range(rows)]

        def explore(i, j):
            if i >= rows or i < 0:
                return
            if j < 0 or j >= cols:
                return
            
            if explored[i][j] == 1:
                return
            if grid[i][j] == "0":
                return
            
            explored[i][j] = 1
            explore(i-1,j)
            explore(i+1,j)
            explore(i,j-1)
            explore(i,j+1)


        for i in range(rows):
            for j in range(cols):
                if explored[i][j] == 1 or grid[i][j] == "0":
                    continue
                else:
                    islands += 1
                    explore(i, j)
        
        return islands
