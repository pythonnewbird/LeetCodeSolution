class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter=collections.Counter(s)
        resultset=set()
        stack=[]
        for c in s:
            counter[c]-=1
            if c in resultset:
                continue
            while stack and stack[-1]>c and counter[stack[-1]]:
                resultset.remove(stack.pop())
            resultset.add(c)
            stack.append(c)
        return ''.join(stack)