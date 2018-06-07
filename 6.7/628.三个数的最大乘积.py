class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = pa = pb = pc = -0x80000000
        na = nb = 0x7FFFFFFF
        for n in nums:
            if n > pa: pa, pb, pc = n, pa, pb
            elif n > pb: pb, pc = n, pb
            elif n > pc: pc = n
            if n < na: na, nb = n, na
            elif n < nb: nb = n
        return max(ans, pa * na * nb, pa * pb * pc)