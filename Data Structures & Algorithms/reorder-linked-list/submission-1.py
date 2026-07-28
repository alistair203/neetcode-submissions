# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        prev, cur = None, slow.next
        slow.next = None
        while cur is not None:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        tail = prev
        while head and tail:
            nexttail = tail.next
            tail.next = head.next
            head.next = tail
            head = tail.next
            tail = nexttail
        return
        



            
        