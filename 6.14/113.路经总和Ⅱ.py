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
        :rtype: List[List[int]]
        """
        res=[]
        self.dfs(root,sum,[],res)
        return res
    def dfs(self,node,sum,path,res):
        if node is None:
            return
        if node.left is None and node.right is None:
            if sum==node.val:
                res.append(path+[node.val])
            return
        path.append(node.val)
        self.dfs(node.left,sum-node.val,path,res)
        self.dfs(node.right,sum-node.val,path,res)
        #需要回溯
        path.pop()
        