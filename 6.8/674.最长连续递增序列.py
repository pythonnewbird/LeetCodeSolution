class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = cnt = 0
        last = None
        for n in nums:
            if n > last:
                cnt += 1
            else:
                ans = max(ans, cnt)
                cnt = 1
            last = n
        return max(ans, cnt)