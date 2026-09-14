class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_rows, num_cols = len(grid), len(grid[0])
        vis = [[False for _ in range(num_cols)] for _ in range(num_rows)]
        directions = [
            [+1, 0],
            [0, +1],
            [-1, 0],
            [0, -1],
        ]

        def dfs(row, col):
            if (
                row < 0 or row >= num_rows or # row out-of-bound
                col < 0 or col >= num_cols or # col out-of-bound
                vis[row][col] == True or # visited before
                grid[row][col] == "0" # water
            ):
                return
            
            vis[row][col] = True

            for drow, dcol in directions:
                nrow, ncol = row + drow, col + dcol
                dfs(nrow, ncol)
        

        cntr = 0
        for row in range(num_rows):
            for col in range(num_cols):
                if vis[row][col] == False and grid[row][col] == "1":
                    cntr += 1
                    dfs(row, col)
        
        return cntr