class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #T[i,j] = number of paths from 0,0 to i,j
        # at i,j only 2 possibilites: colud either come from T[i-1,j] or T[i,j-1]
        # so, T[i,j] = T[i-1,j] + T[i, j-1]
        #base: T[i,0] (first col) = 1
        # T[0,j] (first row) = 1
        # T[0,0] = 1

        T = [[1 for j in range(n)] for i in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                T[i][j] = T[i-1][j] + T[i][j-1]
        
        return T[m-1][n-1]
