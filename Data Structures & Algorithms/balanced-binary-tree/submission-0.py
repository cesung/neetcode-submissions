# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:        
        def dfs(root):
            if not root:
                return True, 0
            
            lb, ll = dfs(root.left)
            rb, rl = dfs(root.right)

            return (
                lb and rb and abs(ll - rl) <= 1,
                max(ll, rl) + 1
            )

        is_balnaced, _ = dfs(root)
        return is_balnaced