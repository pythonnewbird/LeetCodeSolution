# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack=[root]
        count=0
        if not root:
            return 0
        while stack:
            level=[]
            count+=1
            for i in stack:
                if i.left:
                    level.append(i.left)
                if i .right:
                    level.append(i.right)
            stack=level
        return count