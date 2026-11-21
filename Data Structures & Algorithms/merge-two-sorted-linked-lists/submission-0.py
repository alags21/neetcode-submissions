# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # edge cases - 1 list is empty
                    
        if list1 == None:
            if list2 == None:
                return None
            return list2
        
        if list2 == None:
            return list1

        start = list1 if (list1.val < list2.val) else list2
        curr = start
        l1curr = list1
        l2curr = list2
        if l1curr == curr:
            l1curr = l1curr.next
        if l2curr == curr:
            l2curr = l2curr.next
        while (l1curr != None and l2curr != None):
            print(curr.val)

            if (l1curr.val < l2curr.val):
                curr.next = l1curr
                curr = curr.next
                l1curr = l1curr.next
            else:
                curr.next = l2curr
                curr = curr.next
                l2curr = l2curr.next

        if l1curr == None:
            curr.next = l2curr
        else:
            curr.next = l1curr
        
        return start

            
