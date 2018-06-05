class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        odd, even = 0, 0
        for i in range(size):
            if i % 2:
                odd = max(odd + nums[i], even)
            else:
                even = max(even + nums[i], odd)
        return max(odd, even)