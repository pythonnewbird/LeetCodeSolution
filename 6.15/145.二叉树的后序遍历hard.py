# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#使用一个变量c来记录每次弹出的元素，保证元素不会重复进栈
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        stack=[root]
        ans=[]
        c=None
        while stack:
            c=stack[-1]
            if c.left and c.left!=root and c.right!=root:
                stack.append(c.left)
            elif c.right and c.right!=root:
                stack.append(c.right)
            else:
                root=stack.pop()
                ans.append(root.val)
        return ans