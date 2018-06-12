class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0]==1:
            return 0
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dp=[1]
        for i in range(n-1):
            dp.append(0)
        for i in range(0,m):
            for j in range(n):
                if obstacleGrid[i][j]==1:
                    dp[j]=0
                elif j==0:
                    dp[j]=dp[j]
                else:
                    dp[j]=dp[j]+dp[j-1]
        return dp[-1]