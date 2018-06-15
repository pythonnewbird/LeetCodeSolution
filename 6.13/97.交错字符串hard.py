class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        #DFS+记忆化搜索
        r,c,t=len(s1),len(s2),len(s3)
        if (r+c)!=t:
            return False
        stack=[(0,0)]
        visited=set((0,0))
        while stack:
            m,n=stack.pop()
            if m+n==t:
                return True
            if m+1<=r and s1[m]==s3[m+n] and (m+1,n) not in visited:
                stack.append((m+1,n))
                visited.add((m+1,n))
            if n+1<=c and s2[n]==s3[m+n] and (m,n+1) not in visited:
                stack.append((m,n+1))
                visited.add((m,n+1))
        return False