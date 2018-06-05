class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans=0
        x=5
        while n>=x:
            ans += n / x
            x *= 5
        return ans