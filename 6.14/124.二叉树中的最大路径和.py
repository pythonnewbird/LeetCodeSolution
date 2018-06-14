# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self,root):
        if not root:return 0
        maxleft=self.dfs(root.left)
        maxright=self.dfs(root.right)
        maxleft=max(0,maxleft)
        maxright=max(0,maxright)
        self.ans=max(self.ans,maxleft+maxright+root.val)
        #注意返回值与ans的区别
		return max(maxleft,maxright,0)+root.val
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans=None
        self.dfs(root)
        return self.ans
    