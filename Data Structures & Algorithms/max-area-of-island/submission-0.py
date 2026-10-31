class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dir = [[1,0],[0,1],[-1,0],[0,-1]]
        ROWS = len(grid)
        COL = len(grid[0])

        def dfs(r,c):
            res = 0
            if r<0 or c<0 or r>ROWS-1 or c>COL-1 or grid[r][c]==0:
                return 0
            grid[r][c] = 0
            for i in dir:
                res += dfs(r+i[0],c+i[1])
            
            return 1+res

        max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==1:
                    area = dfs(r,c)
                    max_area = max(max_area,area)
        
        return max_area
