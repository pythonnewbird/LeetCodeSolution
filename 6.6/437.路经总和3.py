# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        def traverse(root,val):
            if not root:
                return 0
            res=(root.val==val)
            res+=traverse(root.left,val-root.val)
            res+=traverse(root.right,val-root.val)
            return res
        ans=traverse(root,sum)
        ans+=self.pathSum(root.left,sum)
        ans+=self.pathSum(root.right,sum)
        return ans
        