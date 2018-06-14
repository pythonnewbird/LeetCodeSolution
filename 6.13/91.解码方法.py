class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0 or s[0]=='0': return 0
        cur=ord(s[0])-ord('0')
        a=1
        b=1
        for i in range(1,len(s)):
            pre=ord(s[i-1])-ord('0')
            cur=ord(s[i])-ord('0')
            t=b
            c=0
            if cur==0:
                if pre==0 or pre>2:
                    return 0
                c=a
            elif pre==1:
                c=a+b
            elif pre==2 and cur<7:
                c=a+b
            else:
                c=b
            a=t
            b=c
        return b