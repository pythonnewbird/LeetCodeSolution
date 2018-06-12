class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums: return [[]]
        res=[[]]
        for num in nums:
            res+=[i+[num] for i in res ]
        return res
