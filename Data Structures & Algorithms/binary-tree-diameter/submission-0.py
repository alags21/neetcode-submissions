# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.max_path = float('-inf')

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # for each node, find max on left and right trees and sum them, then compare to global maximum
        self.dfs(root)
        return self.max_path
    
    def dfs(self, curr):
        if not curr:
            return 0
        
        else:
            l_path = self.dfs(curr.left)
            r_path = self.dfs(curr.right)
            self.max_path = max(self.max_path, l_path+r_path)
        
        return max(l_path, r_path) + 1