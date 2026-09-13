# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def getNodePath(root, n, path):
            nonlocal p_path, q_path
            path.append(root)

            if root.val == n.val and n.val == p.val:
                p_path = path[:]
                return
            if root.val == n.val and n.val == q.val:
                q_path = path[:]
                return

            if root.left is not None:
                getNodePath(root.left, n, path)
            if root.right is not None:
                getNodePath(root.right, n, path)
            
            path.pop()
            
        p_path, q_path = [], []
        getNodePath(root, p, [])
        getNodePath(root, q, [])

        ptr = 0
        while (
            ptr < len(p_path) and
            ptr < len(q_path) and
            p_path[ptr].val == q_path[ptr].val
        ):
            ptr += 1
        
        return p_path[ptr - 1]

        
