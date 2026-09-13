class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        num_rows, num_cols = len(board), len(board[0])
        sub_boxes_size = 3
        row_vis = {i : set() for i in range(num_rows)}
        col_vis = {i : set() for i in range(num_cols)}
        sub_boxes_vis = {i : {j : set() for j in range(num_cols // sub_boxes_size)} for i in range(num_rows // sub_boxes_size)}

        for row in range(num_rows):
            for col in range(num_cols):
                if board[row][col] == ".":
                    continue
                val = int(board[row][col])
                if (
                    val in row_vis[row] or
                    val in col_vis[col] or
                    val in sub_boxes_vis[row//sub_boxes_size][col//sub_boxes_size]
                ):
                    return False
                row_vis[row].add(val)
                col_vis[col].add(val)
                sub_boxes_vis[row//sub_boxes_size][col//sub_boxes_size].add(val)
        
        return True
        