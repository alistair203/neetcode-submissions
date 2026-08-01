# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        inorder_idx = {inorder[i]: i for i in range(n)}
        def dfs(l_pre, r_pre, l_in, r_in):
            if l_pre > r_pre or l_in > l_pre:
                return
            node = TreeNode(preorder[l_pre])
            mid_idx = inorder_idx[node.val]
            left_count = min(r_in, mid_idx - 1) - l_in + 1
            node.left = dfs(l_pre + 1, min(r_pre, l_pre + left_count), l_in, min(r_in, mid_idx - 1))
            node.right = dfs(min(r_pre, l_pre + left_count) + 1, r_pre, max(l_in, mid_idx + 1), r_in)
            return node
        return dfs(0, n - 1, 0, n - 1)