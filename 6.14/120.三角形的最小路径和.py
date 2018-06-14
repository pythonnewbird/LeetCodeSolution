class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        dp=triangle[-1]
        height=len(triangle)
        for i in range(height-2,-1,-1):
            for j in range(i+1):
                dp[j]=triangle[i][j]+min(dp[j],dp[j+1])
        return dp[0]