class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        WATER, TREASURE, LAND = -1, 0, 2147483647
        num_rows, num_cols = len(grid), len(grid[0])

        queue = deque()
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == TREASURE:
                    queue.append((row, col, 0))
        directions = [
            [+1, 0],
            [0, +1],
            [-1, 0],
            [0, -1],
        ]
        while queue:
            row, col, dist = queue.popleft()

            for drow, dcol in directions:
                nrow, ncol = row + drow, col + dcol
                
                if (
                    nrow < 0 or nrow >= num_rows or
                    ncol < 0 or ncol >= num_cols
                ):
                    continue
                
                if grid[nrow][ncol] == LAND:
                    grid[nrow][ncol] = dist + 1
                    queue.append( (nrow, ncol, dist + 1) )