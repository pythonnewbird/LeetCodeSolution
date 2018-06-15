class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        #*号不能为0
        if len(s)==0:
            return 0
        d=collections.defaultdict(int)
        for i in range(1,27):
            d[str(i)]=1
        d['*']=9
        d['**']=6+9
        d['1*']=9
        d['2*']=6
        for i in range(7):
            d['*'+str(i)]=2
        d['*7']=d['*8']=d['*9']=1
        
        MOD=10**9+7
        if len(s)==1:
            return d[s[0]]
        elif len(s)==2:
            return d[s]+d[s[0]]*d[s[1]]
        a,b=d[s[0]],d[s[:2]]+d[s[0]]*d[s[1]]
        for i in range(2,len(s)):
            c=(d[s[i]]*b+d[s[i-1:i+1]]*a)%MOD
            a,b=b,c
        return b        