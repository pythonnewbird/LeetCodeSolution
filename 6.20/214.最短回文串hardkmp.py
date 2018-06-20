class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        rev=s[::-1]
        l=s+'#'+rev
        p=[0]*len(l)
        for i in range(1,len(l)):
            j=p[i-1]
            while j>0 and l[i]!=l[j]:
                j=p[j-1]
            p[i]=j+(l[i]==l[j])
        return rev[:len(s)-p[-1]]+s