class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=0: return 0
        count=[0]
        x=0
        while 10**x<=0x7FFFFFFF:
            count.append(count[x]*10+10**x)
            x+=1
        ans=0
        size=len(str(n))
        for digit in str(n):
            digit=int(digit)
            size-=1
            n-=digit*10**size
            if digit==1:
                ans+=n+1+count[size]
            elif digit>1:
                ans+=digit*count[size]+10**size
        return ans
#注意数字n<0的情况