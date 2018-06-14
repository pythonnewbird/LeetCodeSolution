# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        pointer = dummy = TreeNode(None)
        stack = [root]
        while stack:
            top = stack.pop()
            if not top: continue
            stack.append(top.right)
            stack.append(top.left)
            pointer.right = top
            pointer.left = None
            pointer = top
