# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        dp = {} # node, parent_robbed
        def rec(node, parent_robbed):
            if node is None:
                return 0
            if (node, parent_robbed) in dp:
                return dp[(node, parent_robbed)]
            if (node, True) in dp:
                dont_rob = dp[(node, True)]
            else:
                dont_rob = rec(node.left, False) + rec(node.right, False)
                dp[(node, True)] = dont_rob
            if parent_robbed:
                return dont_rob
            res = max(node.val + rec(node.left, True) + rec(node.right, True), dont_rob)
            dp[(node, parent_robbed)] = res
            return res
        return rec(root, False)
            

        