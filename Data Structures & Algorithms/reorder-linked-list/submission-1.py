# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        tail = None
        lstnodes = [curr]
        while curr.next:
            lstnodes.append(curr.next)
            curr = curr.next
        print(lstnodes)
        
        size = len(lstnodes)
        i = 1
        j = size - 1
        curr = lstnodes[0]
        back = True
        while i <= j:
            if back:
                curr.next = lstnodes[j]
                curr = curr.next
                back = False
                j -= 1
            else:
                curr.next = lstnodes[i]
                curr = curr.next
                back = True
                i += 1

        curr.next = None
