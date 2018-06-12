class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len=0
        stack=[]
        k=-1
        for i,b in enumerate(s):
            if b=='(':
                stack.append(i)
            elif stack:
                stack.pop()
                if stack:
                    l=i-stack[-1]
                else:
                    l=i-k
                if l>max_len:
                    max_len=l
            else:
                k=i
        return max_len