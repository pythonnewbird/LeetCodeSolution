# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        left, right, val = root.left, root.right, root.val
        return max(self.longestPath(left, val) + self.longestPath(right, val), \
            self.longestUnivaluePath(left), \
            self.longestUnivaluePath(right))
    def longestPath(self, root, val):
        if not root or root.val != val: return 0
        return 1 + max(self.longestPath(root.left, val), self.longestPath(root.right, val))