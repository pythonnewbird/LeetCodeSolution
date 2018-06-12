class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res=[]
        def helper(left,right,path):
            if right<left:
                return
            if not left and not right:
                res.append(path)
            if left:
                helper(left-1,right,path+'(')
            if right:
                helper(left,right-1,path+')')
        helper(n,n,'')
        return res