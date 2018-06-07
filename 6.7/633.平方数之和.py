class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        for a in range(int(c ** 0.5) + 1):
            b2 = c - a ** 2
            if (int(b2 ** 0.5)) ** 2 == b2:
                return True
        return False