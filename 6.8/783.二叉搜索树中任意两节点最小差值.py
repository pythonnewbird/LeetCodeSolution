# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = 0x7FFFFFFF
        if root.left:
            lmax = root.left
            while lmax.right: lmax = lmax.right
            ans = min(ans, root.val - lmax.val)
            ans = min(ans, self.minDiffInBST(root.left))
        if root.right:
            rmin = root.right
            while rmin.left: rmin = rmin.left
            ans = min(ans, rmin.val - root.val)
            ans = min(ans, self.minDiffInBST(root.right))
        return ans