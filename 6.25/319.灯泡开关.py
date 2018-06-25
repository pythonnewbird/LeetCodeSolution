class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(math.sqrt(n))
		
因为除了完全平方数，其余数字的因子都是成对出现的，而完全平方数的平方根只会统计一次。