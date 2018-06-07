class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        n = abs(num)
        ans = ''
        while n:
            ans += str(n % 7)
            n /= 7
        return ['', '-'][num < 0] + ans[::-1] or '0'