class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=[1]+nums+[1]
        n=len(nums)
        dp=[[0]*n for _ in range(n)]
        def helper(i,j):
            if dp[i][j] or j-i==1:
                return dp[i][j]
            
            for k in range(i+1,j):
                dp[i][j]=max(dp[i][j],nums[i]*nums[k]*nums[j]+helper(i,k)+helper(k,j))
            return dp[i][j]
        return helper(0,n-1)
		
		
Bottom-up:

 class Solution(object):
        def maxCoins(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            nums = [1] + nums + [1] # build the complete array 
            n = len(nums)
            dp = [[0] * n for _ in xrange(n)]
    
            for gap in xrange(2, n):
                for i in xrange(n-gap):
                    j = i + gap
                    for k in xrange(i+1, j):
                        dp[i][j] = max(dp[i][j], nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j])
            return dp[0][n-1]
			
以最后被爆破的气球m为界限，把数组分为左右两个子区域

状态转移方程：

dp[l][r] = max(dp[l][r], nums[l] * nums[m] * nums[r] + dp[l][m] + dp[m][r])
dp[l][r]表示扎破(l, r)范围内所有气球获得的最大硬币数，不含边界；

l与r的跨度k从2开始逐渐增大；

三重循环依次枚举范围跨度k，左边界l，中点m；右边界r = l + k；