# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0
        stk  = [-101]

        def dfs(root, stk):
            nonlocal good

            if stk[-1] <= root.val:
                good += 1
            
            stk.append(max(stk[-1], root.val))

            if root.left is not None:
                dfs(root.left, stk)
            if root.right is not None:
                dfs(root.right, stk)
            
            stk.pop()
        
        dfs(root, stk)

        return good
