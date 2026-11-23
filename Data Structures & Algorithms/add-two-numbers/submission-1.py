# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # want to build the integers from the front of each list, having a multiplier using 10^power

        power = 0
        l1_tot = 0
        l2_tot = 0
        l1_curr = l1
        l2_curr = l2

        while l1_curr or l2_curr:
            if l1_curr:
                l1_tot += l1_curr.val * (10**power)
                l1_curr = l1_curr.next
            if l2_curr:
                l2_tot += l2_curr.val * (10**power)
                l2_curr = l2_curr.next
            power += 1

        total = l1_tot + l2_tot

        # now we need to construct a linked list for this integer, total
        # we can use modulus 10 to get the last digit, add a node in the linked list
        # then divide by 10 to remove the last digit

        curr = ListNode()
        head = curr
        while total != 0:
            curr.val = total % 10
            total  = int(total//10)
            if total != 0:
                curr.next = ListNode()
                curr = curr.next

        return head