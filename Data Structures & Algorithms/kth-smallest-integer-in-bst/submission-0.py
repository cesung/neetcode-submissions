# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cur = root
        stk = []
        n = 0

        while cur or stk:
            while cur:
                stk.append(cur)
                cur = cur.left
            
            # reach here if cur is None
            cur = stk.pop()

            n += 1
            if n == k:
                return cur.val

            cur = cur.right
        
        return -1