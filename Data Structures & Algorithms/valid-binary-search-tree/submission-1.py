# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, lbound, rbound):
            if not root:
                return True

            return (
                lbound < root.val < rbound and
                dfs(root.left, lbound, root.val) and
                dfs(root.right, root.val, rbound)
            )
        
        return dfs(root, float("-inf"), float("inf"))