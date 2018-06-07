# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.last = -0x80000000
        self.ans = 0x7FFFFFFF
        def inOrderTraverse(root):
            if not root: return
            inOrderTraverse(root.left)
            self.ans = min(self.ans, root.val - self.last)
            self.last = root.val
            inOrderTraverse(root.right)
        inOrderTraverse(root)
        return self.ans        
