# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels,level=[],[root]
        while level and root:
            levels.append([node.val for node in level])
            level=[kid for node in level for kid in (node.left,node.right) if kid]
        return levels[::-1]