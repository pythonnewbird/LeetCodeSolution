# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.total = 0
        def traverse(root):
            if not root: return
            traverse(root.right)
            root.val += self.total
            self.total = root.val
            traverse(root.left)
        traverse(root)
        return root