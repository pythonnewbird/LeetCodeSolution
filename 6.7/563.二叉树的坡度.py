# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        def subTreeSum(root):
            if not root: return 0
            lsum = subTreeSum(root.left)
            rsum = subTreeSum(root.right)
            self.ans += abs(lsum - rsum)
            return root.val + lsum + rsum
        subTreeSum(root)
        return self.ans