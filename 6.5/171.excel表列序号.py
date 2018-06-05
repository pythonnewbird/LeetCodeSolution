class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        for e in s:
            ans = ans * 26 + ord(e) - ord('A') + 1
        return ans