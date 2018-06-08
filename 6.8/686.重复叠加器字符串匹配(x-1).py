class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        sa, sb = len(A), len(B)
        x = 1
        while (x-1)* sa <= 2 * max(sa, sb):
            if B in A * x: return x
            x += 1
        return -1