# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#O(K)
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack=[]
        count=0
        while len(stack) or root:
            if root:
                stack.append(root)
                root=root.left
            else:
                node=stack.pop()
                count+=1
                if count==k:
                    return node.val
                else:
                    root=node.right
        return None
#O(height)
class Solution(object):
    def caculate(self, root):
        """
        caculate the tree's sons
        """
        if root == None:
            return 0
        else:
            return 1 + self.caculate(root.left) + self.caculate(root.right)
    
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if root == None:
            return 0
        left_size = self.caculate(root.left)
        if k == left_size + 1:
            return root.val
        elif k < left_size + 1:
            return self.kthSmallest(root.left, k)
        elif k > left_size + 1:
            return self.kthSmallest(root.right, k-left_size-1)