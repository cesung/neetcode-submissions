# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        idx_lookup = {val:i for i, val in enumerate(inorder)}
        pre_idx = 0

        def _build_tree(l, r):
            nonlocal pre_idx

            if l >= r:
                return None

            rt_val = preorder[pre_idx]
            rt_idx = idx_lookup[rt_val]

            pre_idx += 1
            root = TreeNode(rt_val)
            root.left = _build_tree(l, rt_idx)
            root.right = _build_tree(rt_idx+1, r)

            return root

        return _build_tree(0, n)