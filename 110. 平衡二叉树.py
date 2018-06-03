# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfsHeight(root)!=-1
    def dfsHeight(self,root):
        if not root: return 0
        left=self.dfsHeight(root.left)
        if left==-1:
            return -1
        right=self.dfsHeight(root.right)
        if right==-1:
            return -1
        if abs(left-right)>1:return -1
        return max(left,right)+1