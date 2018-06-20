class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack=[0]
        signs=[1]
        sign=1
        n=0
        ans=0
        for c in '({})'.format(s):
            if c.isdigit():
                n=n*10+ord(c)-ord('0')
            elif c=='+':
                stack[-1]+=n*sign
                n,sign=0,1
            elif c=='-':
                stack[-1]+=n*sign
                sign,n=-1,0
            elif c=='(':
                stack.append(0)
                signs.append(sign)
                sign=1
            elif c==')':
                stack[-1]+=sign*n
                n,sign=stack.pop(),signs.pop()
                stack[-1]+=sign*n
                sign,n=1,0
        for sign,n in zip(signs,stack):
            ans+=n*sign
        return ans
                