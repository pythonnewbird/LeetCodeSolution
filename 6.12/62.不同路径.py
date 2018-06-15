class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m < n:
            m, n = n, m
        dp = [0] * n
        dp[0] = 1
        for x in range(m):
            for y in range(n - 1):
                dp[y + 1] += dp[y]
        return dp[n - 1]