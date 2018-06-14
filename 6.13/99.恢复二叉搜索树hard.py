# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.pre=None
        self.p1=None
        self.p2=None
    def inorder(self,root):
        if not root: return
        self.inorder(root.left)
        if self.pre and root.val<self.pre.val:
            if not self.p1:
                self.p1=self.pre
            self.p2=root
        self.pre=root
        self.inorder(root.right)
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.inorder(root)
        self.p1.val,self.p2.val=self.p2.val,self.p1.val