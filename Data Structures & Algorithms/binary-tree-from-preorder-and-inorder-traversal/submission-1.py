# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        in_idx = {inorder[i]: i for i in range(len(inorder))}
        nodes = {n: TreeNode(n) for n in preorder}
        i = 1
        def predfs(parent, lb, ub):
            nonlocal i
            if i == len(inorder):
                return
            to_traverse = []
            child = preorder[i]
            if lb < in_idx[child] < min(ub, in_idx[parent.val]):
                if parent.left is None:
                    parent.left = nodes[child]
                    i += 1
                    if i == len(inorder):
                        return
                    child = preorder[i]
                to_traverse.append((parent.left, lb, min(ub, in_idx[parent.val])))
            if max(lb, in_idx[parent.val]) < in_idx[child] < ub:
                if parent.right is None:
                    parent.right = nodes[child]
                    i += 1
                to_traverse.append((parent.right, max(lb, in_idx[parent.val]), ub))
            for triple in to_traverse:
                predfs(*triple)
        while i < len(inorder):
            predfs(nodes[preorder[0]], -float("inf"), float("inf"))
        return nodes[preorder[0]]

            
        