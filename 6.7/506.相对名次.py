class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        dmap = {v : k for k, v in enumerate(sorted(nums, reverse=True))}
        return [str(dmap[n] + 1)  if dmap[n] > 2 else ['Gold', 'Silver', 'Bronze'][dmap[n]] + ' Medal' for n in nums]
        