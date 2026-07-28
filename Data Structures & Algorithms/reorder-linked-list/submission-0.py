# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []
        n = 0
        while head is not None:
            nodes.append(head)
            head = head.next
            n += 1
        l, r = 0, n - 1
        cur = ListNode()
        while r - l > 1:
            cur.next = nodes[l]
            cur = cur.next
            cur.next = nodes[r]
            cur = cur.next
            l += 1
            r -= 1
        cur.next = nodes[l]
        cur = cur.next
        if r - l == 1:
            cur.next = nodes[r]
            cur = cur.next
        cur.next = None
        return