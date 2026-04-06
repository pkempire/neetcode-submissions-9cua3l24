class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = 0
        def dfs(r,c):
            if r<0 or c<0 or r >= len(grid) or c >= len(grid[0]):
                return
            if grid[r][c] == "0":
                return    
            if (r,c) in visited:
                return

            visited.add ((r,c))
            dfs(r+1, c)
            dfs (r-1, c)
            dfs(r,c+1)
            dfs(r,c-1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    islands +=1
                    dfs(i,j)

        return islands