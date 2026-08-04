"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        copies = {None: None}
        def dfs_copy(n):
            if n in copies:
                return
            copies[n] = Node(n.val)
            for neighbour in n.neighbors:
                dfs_copy(neighbour)
        linked = set()
        def dfs_link_neighbors(n):
            if n is None or n in linked:
                return
            linked.add(n)
            for neighbour in n.neighbors:
                copies[n].neighbors.append(copies[neighbour])
                dfs_link_neighbors(neighbour)
        dfs_copy(node)
        dfs_link_neighbors(node)
        return copies[node]
        