# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans=[]
        if not root: return ans
        level=[root]
        mark=True
        while level:
            if mark:
                result=[i.val for i in level]
            else:
                result=[i.val for i in level[::-1]]
            ans.append(result)
            mark=not mark
            tmp=[]
            for node in level:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            level=tmp
        return ans