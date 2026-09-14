class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        num_rows, num_cols = len(grid), len(grid[0])
        vis = [[False for _ in range(num_cols)] for _ in range(num_rows)]
        directions = [
            [+1, 0],
            [0, +1],
            [-1, 0],
            [0, -1]
        ]

        fresh = set()
        queue = deque()
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == 1:
                    fresh.add( (row, col) )
                elif grid[row][col] == 2:
                    queue.append( (row, col) )
                    
        if not fresh:
            return 0

        dist = 0
        while queue:

            for _ in range(len(queue)):
                row, col = queue.popleft()

                for drow, dcol in directions:
                    nrow, ncol = row + drow, col + dcol
                    
                    if (
                        nrow < 0 or nrow >= num_rows or
                        ncol < 0 or ncol >= num_cols or
                        vis[nrow][ncol] == True
                    ):
                        continue
                    
                    # mark cell as visited
                    vis[nrow][ncol] = True
                    
                    if grid[nrow][ncol] == 1:
                        fresh.remove( (nrow, ncol) )
                        queue.append( (nrow, ncol) )
                    
            if not fresh:
                return dist + 1
            
            dist += 1

        return -1
