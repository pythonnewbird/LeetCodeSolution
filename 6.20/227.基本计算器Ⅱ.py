class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack=[]
        num=0
        pre='+'
        s=s+'+'
        for n in s:
            if n.isdigit():
                num=num*10+ord(n)-ord('0')
            elif n==' ':
                continue
            else:
                if pre=='+':
                    stack.append(num)
                elif pre=='-':
                    stack.append(-num)
                elif pre=='*':
                    stack[-1]*=num
                else:
                    stack[-1]=int(stack[-1]*1.0/num)
                pre=n
                num=0
        return sum(stack)