class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n = bin(n)
        return all (n[x] != n[x + 1] for x in range(len(n) - 1))
        