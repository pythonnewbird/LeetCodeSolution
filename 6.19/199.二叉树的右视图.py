# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def rightSideView(self, root):
        ans = []
        if root is None:
            return ans
        queue = [root]
        while queue:
            size = len(queue)
            for r in range(size):
                top = queue.pop(0)
                if r == 0:
                    ans.append(top.val)
                if top.right:
                    queue.append(top.right)
                if top.left:
                    queue.append(top.left)
        return ans