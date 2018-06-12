class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        if len(dungeon)==0: return
        m,n=len(dungeon),len(dungeon[0])
        dp=[[0]*n for _ in range(m)]
        hp=0
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if (i<m-1) and (j<n-1):
                    hp=min(dp[i+1][j]-dungeon[i][j],dp[i][j+1]-dungeon[i][j])
                elif i<m-1:
                    hp=dp[i+1][j]-dungeon[i][j]
                elif j<n-1:
                    hp=dp[i][j+1]-dungeon[i][j]
                else:
                    hp=1-dungeon[-1][-1]
                
                if (hp<=0):
                    hp=1
                dp[i][j]=hp
        return dp[0][0]
#44ms，超越100%        