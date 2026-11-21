# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        res = []
        d = deque([root])

        while d:
            level_size = len(d)
            curr = 0
            res.append([])
            while (curr < level_size and d):
                node = d.popleft()
                res[-1].append(node.val)
                curr += 1
                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)
        return res
