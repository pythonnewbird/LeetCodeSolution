# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        d={}
        stack=[]
        for i,val in enumerate(inorder):
            d[val]=i
        root=parent=None
        for i in preorder:
            node=TreeNode(i)
            if not root:
                root=node
            elif d[i]<d[parent.val]:
                parent.left=node
                stack.append(parent)
            elif d[i]>d[parent.val]:
                while stack and d[stack[-1].val]<d[i]:
                    parent=stack.pop()
                parent.right=node
            parent=node
        return root
