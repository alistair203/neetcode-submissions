# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        if current is None:
            return current
        nex = current.next
        current.next = None
        while nex is not None:
            prev = current
            current = nex
            nex = current.next
            current.next = prev
        return current


        