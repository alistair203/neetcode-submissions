# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque()
        if root is not None:
            q.appendleft(root)
        while q:
            for _ in range(len(q)):
                node = q.pop()
                if node.left:
                    q.appendleft(node.left)
                if node.right:
                    q.appendleft(node.right)
            res.append(node.val)
        return res