# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        cur = head
        for i in range(left - 2):
            cur = cur.next
        if left > 1:
            before_left = cur
            cur = cur.next
        prev, cur = cur, cur.next
        for i in range(right - left):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        if left > 1:
            before_left.next.next = cur
            before_left.next = prev
            return head
        else:
            head.next = cur
            return prev

