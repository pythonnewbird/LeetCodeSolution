class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        size=len(s)
        next=[0]*size
        
        for i in range(1,size):
            k=next[i-1]
            while s[i]!=s[k] and k:
                k=next[k-1]
            if s[k]==s[i]:
                next[i]=k+1
        p=next[-1]
        return p > 0 and size % (size - p) == 0

记字符串长度为size

利用KMP算法求next数组，记next数组的最后一个元素为p

若p > 0 并且 size % (size - p) == 0，返回True

next数组具有如下性质：

str[ 0 : next[i] ] == str[ i + 1 - next[i] : i + 1 ]

例如：

a, b, c, d, a, b, c, a, b, c, d, a, b, c, d, c

0, 0, 0, 0, 1, 2, 3, 1, 2, 3, 4, 5, 6, 7, 4, 0