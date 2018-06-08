# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False
        check=[root]
        s=set()
        for i in check:
            if k-i.val in s:
                return True
            s.add(i.val)
            if i.left:
                check.append(i.left)
            if i.right:
                check.append(i.right)
        return False