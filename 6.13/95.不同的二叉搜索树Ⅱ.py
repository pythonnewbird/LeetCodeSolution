# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n==0: return []
        dp={}
        def get_tree(n,m):
            if (n,m) in dp:
                return dp[(n,m)]
            if n>m:
                return [None]
            res=[]
            for i in range(n,m+1):
                for left in get_tree(n,i-1):
                    for right in get_tree(i+1,m):
                        tmp,tmp.left,tmp.right=TreeNode(i),left,right
                        res.append(tmp)
            dp[(n,m)]=res
            return res
        return get_tree(1,n)