class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=set(nums)
        a=sum(a)*3-sum(nums)
        a=a/2
        return a