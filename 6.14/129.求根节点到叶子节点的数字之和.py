# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root,val):
            val=val*10+root.val
            if (root.left or root.right) is None:
                return val
            sums=0
            if root.left:
                sums+=dfs(root.left,val)
            if root.right:
                sums+=dfs(root.right,val)
            return sums
        if not root: return 0
        return dfs(root,0)