class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        num_rows, num_cols = len(grid), len(grid[0])
        vis = [[False for _ in range(num_cols)] for _ in range(num_rows)]
        directions = [
            [+1, 0],
            [0, +1],
            [-1, 0],
            [0, -1],
        ]
        max_area = 0

        def dfs(row, col):
            if (
                row < 0 or row >= num_rows or
                col < 0 or col >= num_cols or
                grid[row][col] == 0 or
                vis[row][col] == True
            ):
                return 0

            vis[row][col] = True
            area = 1

            for drow, dcol in directions:
                nrow, ncol = row + drow, col + dcol
                area += dfs(nrow, ncol)
            
            return area


        for row in range(num_rows):
            for col in range(num_cols):
                if (
                    vis[row][col] or # once visited
                    grid[row][col] == 0 # water
                ):
                    continue
                
                max_area = max(
                    max_area,
                    dfs(row, col)
                )
        
        return max_area