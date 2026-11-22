# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        nodes = 0
        while curr:
            curr = curr.next
            nodes += 1
        curr = head
        prev = None
        i = 1
        while i < nodes-n+1:
            prev = curr
            curr = curr.next
            i += 1
        if curr == head:
            head = curr.next
            return head
        if not curr.next:
            prev.next = None
            return head

        prev.next = curr.next
        return head
        # i=1: prev = 1, curr = 2
        # i=2 break
        # prev.next = curr.next.next
        # 1