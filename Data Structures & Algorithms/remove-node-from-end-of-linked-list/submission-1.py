# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sz = 0
        cur = head
        while cur is not None:
            sz += 1
            cur = cur.next
        cur = head
        counter = 1
        if sz == 1:
            return None
        if n == sz:
            return head.next
        while counter < sz - n:
            cur = cur.next
            counter += 1
        cur.next = cur.next.next
        return head

        