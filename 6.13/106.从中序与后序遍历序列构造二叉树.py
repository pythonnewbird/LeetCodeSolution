# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self,inorder):
        if not self.postorder or not inorder:
            return None
        tmp=self.postorder.pop()
        root = TreeNode(tmp)
        #要先right后left
        root.right=self.helper(inorder[inorder.index(root.val)+1:])
        root.left=self.helper(inorder[:inorder.index(root.val)])
        
        return root
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        self.postorder = postorder
        return self.helper(inorder)
