# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # compute height of right tree, left tree, and return if the difference is greater than  1

        # use postorder DFS - compute left, right, then current

        if not root:
            return True

        stack = [root]
        output = []
        heights = {None : 0}

        while stack:
            node = stack.pop()
            output.append(node)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            
        while output:
            node = output.pop()
            left = heights[node.left]
            right = heights[node.right]

            if abs(left - right) > 1:
                return False
            heights[node] = max(left,right) + 1
        return True
