class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        return max(self.robLinear(nums[1:]), self.robLinear(nums[:-1]))
        
    # @param num, a list of integer
    # @return an integer
    def robLinear(self, num):
        size = len(num)
        odd, even = 0, 0
        for i in range(size):
            if i % 2:
                odd = max(odd + num[i], even)
            else:
                even = max(even + num[i], odd)
        return max(odd, even)