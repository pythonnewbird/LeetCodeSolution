# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root in (None,q,p):
            return root
        if self.isParent(p,q):
            return p
        if self.isParent(q,p):
            return q
        while root:
            if self.isParent(root.left,p) and self.isParent(root.left,q):
                root=root.left
            elif self.isParent(root.right,p) and self.isParent(root.right,q):
                root=root.right
            else:
                return root
        return root
    def isParent(self,p,q):
        if not p:
            return False
        if p==q:
            return True
        return self.isParent(p.left,q) or self.isParent(p.right,q)
            