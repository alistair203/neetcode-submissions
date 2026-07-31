# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        target = None
        cur = root
        dummy = TreeNode(float("inf"), root)
        prev = dummy
        while cur:
            if cur.val == key:
                target = cur
                break
            prev = cur
            if key < cur.val:
                cur = cur.left
            else:
                cur = cur.right
        if target is not None:
            to_reinsert = target.left
            if key < prev.val:
                prev.left = target.right
            else:
                prev.right = target.right
            if to_reinsert is not None:
                cur = target.right
                while cur:
                    prev = cur
                    if to_reinsert.val < cur.val:
                        cur = cur.left
                    else:
                        cur = cur.right
                if val < prev.val:
                    prev.left = to_reinsert
                else:
                    prev.right = to_reinsert
        return dummy.left
        