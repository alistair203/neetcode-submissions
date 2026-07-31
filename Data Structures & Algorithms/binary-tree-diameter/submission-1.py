# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def max_depth(node):
            nonlocal res
            if node is None:
                return 0
            left = max_depth(node.left)
            right = max_depth(node.right)
            res = max(res, left + right)
            return 1 + max(left, right)
        max_depth(root)
        return res
        