class Solution(object):
    def __init__(self):
        MAXN = 100
        self.prime = [1] * (MAXN + 1)
        self.prime[0] = self.prime[1] = 0
        for x in range(2, MAXN + 1):
            if self.prime[x]:
                y = x ** 2
                while y <= MAXN:
                    self.prime[y] = 0
                    y += x
    def countPrimeSetBits(self, L, R):
        """
        :type L:     
        :type R:     
        :rtype:     
        """
        ans = 0
        for x in range(L, R + 1):
            ans += self.prime[bin(x).count('1')]
        return ans