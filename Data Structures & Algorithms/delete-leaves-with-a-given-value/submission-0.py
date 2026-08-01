# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        self.target = target
        def is_leaf(node):
            return node and not (node.left or node.right)
        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            dfs(node.right)
            if is_leaf(node.left) and node.left.val == self.target: 
                node.left = None
            if is_leaf(node.right) and node.right.val == self.target:
                node.right = None
        dfs(root)
        if is_leaf(root) and root.val == target:
            return None
        return root
            

        