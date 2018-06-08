class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        p = [[0 for x in xrange(len(s))] for y in xrange(len(s))] 
        max_length,x,y = 0,0,0
        for i in xrange(0,len(s)):
            for j in xrange(0,len(s)-i):
                if i == 0:p[j][j] = 1
                elif i == 1:p[j][j+i] = s[j] == s[j+i]
                else:p[j][j+i] = p[j+1][j+i-1] and s[j] == s[j+i]         
                if p[j][j+i] and i >= max_length:
                    max_length = i
                    x,y = j,j+i+1   
        return s[x:y]