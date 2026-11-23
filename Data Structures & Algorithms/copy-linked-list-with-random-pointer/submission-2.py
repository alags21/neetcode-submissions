"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # each node needs: next pointer to new node, random pointer to random node
        # iterate through each node in the original LL
            # assign each node to a hashmap - key = old node, value = new node
            # on second pass, assign new node random -> old node vlaue in hash
                    
        if not head:
            return None
        old_to_new = {}
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val, curr.next, curr.random)
            curr = curr.next

        curr = old_to_new[head]
        while curr:
            if curr.next:
                curr.next = old_to_new[curr.next]
            if curr.random:
                curr.random = old_to_new[curr.random]
            curr = curr.next
        
        return old_to_new[head]


