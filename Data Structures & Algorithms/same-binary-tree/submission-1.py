# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.appendleft((p, q))
        while queue:
            nodes = queue.pop()
            if nodes[0] is None and nodes[1] is None:
                continue
            if (
                (nodes[0] is None and nodes[1] is not None) or
                (nodes[0] is not None and nodes[1] is None) or
                (nodes[0].val != nodes[1].val)
            ):
                return False
            queue.appendleft((nodes[0].left, nodes[1].left))
            queue.appendleft((nodes[0].right, nodes[1].right))
        return True
            
        