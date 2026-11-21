# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.depth(root)

    def depth(self, node):
        #base case: node doesn't exist
        if node == None:
            return 0
        # children exist

        ld = self.depth(node.left)
        rd = self.depth(node.right)
    
        return 1 + max(ld, rd)