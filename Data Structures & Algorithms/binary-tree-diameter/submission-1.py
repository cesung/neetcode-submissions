# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def dfs(root):
            nonlocal diameter

            if not root:
                return 0

            ll = dfs(root.left)
            rl = dfs(root.right)

            diameter = max(
                diameter,
                ll + rl
            )

            return max(ll, rl) + 1

        dfs(root)

        return diameter