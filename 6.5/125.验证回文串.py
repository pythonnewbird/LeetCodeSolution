class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()
        s=''.join([i for i in s if i.isalpha() or i.isdigit()])
        return s==s[::-1]