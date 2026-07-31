# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # (val ,lb, ub)
        q = deque()
        if root is not None:
            q.appendleft((root, -float("inf"), float("inf")))
        while q:
            node, lb, ub = q.pop()
            if not (lb < node.val < ub):
                return False
            if node.left:
                q.appendleft((node.left, lb, min(ub, node.val)))
            if node.right:
                q.appendleft((node.right, max(lb, node.val), ub))
        return True