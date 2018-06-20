class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = sorted([str(x) for x in nums], cmp = self.compare)
        ans = ''.join(nums).lstrip('0')
        return ans or '0'

    def compare(self, a, b):
        return [1, -1][a + b > b + a]