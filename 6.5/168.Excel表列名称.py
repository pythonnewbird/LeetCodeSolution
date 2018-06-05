class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = ''
        while n:
            ans = chr(ord('A') + (n - 1) % 26) + ans
            n = (n - 1) / 26
        return ans
        