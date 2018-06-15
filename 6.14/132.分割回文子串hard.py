class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if not s: return 0
        dp=[0]*len(s)
        p=[[False for i in range(len(s))] for j in range(len(s))]
        for i in range(len(s)):
            dp[i]=float('inf')
            for j in range(i,-1,-1):
                if s[i]==s[j] and (i-j<2 or p[j+1][i-1]):
                    p[j][i]=True
                    dp[i]=min(dp[i],0 if j==0 else dp[j-1]+1)
        return dp[-1]