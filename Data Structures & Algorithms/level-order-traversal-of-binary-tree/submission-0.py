# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = deque([root])

        while queue:
            vals = []
            for i in range(len(queue)):
                n = queue.popleft()
                vals.append(n.val)

                if n.left is not None:
                    queue.append(n.left)
                if n.right is not None:
                    queue.append(n.right)
            
            res.append(vals)

        return res

