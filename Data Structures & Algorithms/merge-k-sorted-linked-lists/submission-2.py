# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # start at a dummy node
        # iterate through all lists
        # find the minimum across all first nodes in each list
        # add that to the existing list
        # advance that list's node


        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                merged.append(self.conquer(l1, l2))
            lists = merged

        return lists[0]
    
    def conquer(self, l1, l2):
        dummy = ListNode()
        curr = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        if l1:
            curr.next = l1
        else:
            curr.next = l2
        
        return dummy.next



        # dummy = ListNode()
        # curr = dummy

        # while True:
        #     curr_min = float('inf')
        #     curr_min_node = None
        #     min_index = None
        #     list_index = 0
        #     for l in lists:
        #         if l:
        #             if l.val < curr_min:
        #                 curr_min = l.val
        #                 curr_min_node = l
        #                 min_index = list_index
        #         list_index += 1

        #     if not curr_min_node:
        #         break

        #     curr.next = lists[min_index]
        #     lists[min_index] = lists[min_index].next
        #     curr = curr.next
        # return dummy.next