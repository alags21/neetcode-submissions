# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.cnt = 0
        self.target = 0
        self.ans = -1
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # we can do an inorder traversal
        self.target = k
        self.inorder(root)
        return self.ans
    
    def inorder(self, curr: Optional[TreeNode]):
        if curr is None:
            return
        self.inorder(curr.left)
        self.cnt += 1
        if (self.cnt == self.target):
            self.ans = curr.val
        self.inorder(curr.right)

