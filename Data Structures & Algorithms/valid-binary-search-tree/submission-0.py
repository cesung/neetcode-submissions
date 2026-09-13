# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root is None:
                return float('-inf'), float('inf'), True

            lmax, lmin, lsuc = dfs(root.left)
            rmax, rmin, rsuc = dfs(root.right)

            return (
                max(lmax, rmax, root.val),
                min(lmin, rmin, root.val),
                (
                    lsuc and
                    rsuc and
                    lmax < root.val < rmin
                )
            )

        _, _, suc = dfs(root)
        return suc