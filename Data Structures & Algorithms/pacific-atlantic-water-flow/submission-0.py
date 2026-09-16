class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        num_rows, num_cols = len(heights), len(heights[0])
        reach_pacific, reach_atlantic = set(), set()
        pacific, atlantic = set(), set()

        for row in range(num_rows):
            pacific.add((row, 0))
            atlantic.add((row, num_cols - 1))
            
        for col in range(num_cols):
            pacific.add((0, col))
            atlantic.add((num_rows - 1, col))
        
        directions = [
            [+1, 0],
            [0, +1],
            [-1, 0],
            [0, -1],
        ]

        def dfs(row, col, reach):
            reach.add((row, col))
            
            for drow, dcol in directions:
                nrow, ncol = row + drow, col + dcol

                if (
                    nrow < 0 or nrow >= num_rows or
                    ncol < 0 or ncol >= num_cols or
                    heights[nrow][ncol] < heights[row][col] or
                    (nrow, ncol) in reach
                ):
                    continue
                
                dfs(nrow, ncol, reach)
        
            return
                

        for row, col in pacific:
            dfs(row, col, reach_pacific)

        for row, col in atlantic:
            dfs(row, col, reach_atlantic)
        
        res = []
        for row in range(num_rows):
            for col in range(num_cols):
                if (
                    (row, col) in reach_pacific and
                    (row, col) in reach_atlantic
                ):
                    res.append([row, col])
            
        return res
