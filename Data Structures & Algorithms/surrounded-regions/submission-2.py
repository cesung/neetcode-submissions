class Solution:
    def solve(self, board: List[List[str]]) -> None:
        num_rows, num_cols = len(board), len(board[0])
        queue = deque([
            (row, col)
            for row in range(num_rows)
            for col in range(num_cols)
            if (
                (row in {0, num_rows - 1} or col in {0, num_cols - 1}) and
                board[row][col] == 'O'
            )
        ])

        directions = [
            [+1, 0],
            [0, +1],
            [-1, 0],
            [0, -1]
        ]

        while queue:
            row, col = queue.popleft()
            board[row][col] = '#'
            for drow, dcol in directions:
                nrow, ncol = row + drow, col + dcol

                if (
                    nrow < 0 or nrow >= num_rows or
                    ncol < 0 or ncol >= num_cols or
                    board[nrow][ncol] != 'O'
                ):
                    continue
                queue.append( (nrow, ncol) )
        
        for row in range(num_rows):
            for col in range(num_cols):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == '#':
                    board[row][col] = 'O'