# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # curr = head
        # nodes = 0
        # while curr:
        #     curr = curr.next
        #     nodes += 1
        # curr = head
        # prev = None
        # i = 1
        # while i <= nodes-n:
        #     prev = curr
        #     curr = curr.next
        #     i += 1
        # if curr == head:
        #     head = curr.next
        #     return head
        # if not curr.next:
        #     prev.next = None
        #     return head

        # prev.next = curr.next
        # return head

        # TWO POINTER APPROACH:
        # move a fast pointer n steps ahead
        # move slow pointer together
        # when right pointer.next is None, left pointer is just before removal node
        dummy = ListNode(0, head)
        slow = dummy
        fast = head
        i = 0
        while n > 0:
            fast = fast.next
            n -= 1

        while fast:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return dummy.next
    
