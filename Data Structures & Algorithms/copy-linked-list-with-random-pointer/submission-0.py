"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        cur = head
        cur_copy = Node(head.val)
        copies = {cur: cur_copy}
        while cur.next is not None:
            cur = cur.next
            cur_copy.next = Node(cur.val)
            cur_copy = cur_copy.next
            copies[cur] = cur_copy
        cur = head
        while cur is not None:
            if cur.random is not None:
                copies[cur].random = copies[cur.random]
            cur = cur.next
        return copies[head]

        