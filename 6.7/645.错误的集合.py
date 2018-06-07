class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        m = len(nums)
        dmap = [0] * m
        for n in nums:
            if not dmap[n - 1]: dmap[n - 1] = 1
            else: return [n, (1 + m) * m / 2 + n - sum(nums)]