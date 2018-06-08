class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        isPalindrome = lambda s: s == s[::-1]
        strPart = lambda s, x: s[:x] + s[x + 1:]
        size = len(s)
        lo, hi = 0, size - 1
        while lo < hi:
            if s[lo] != s[hi]:
                return isPalindrome(strPart(s, lo)) or isPalindrome(strPart(s, hi))
            lo += 1
            hi -= 1
        return True