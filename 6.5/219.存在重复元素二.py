class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        numdict={}
        for i in range(len(nums)):
            idx=numdict.get(nums[i])
            if idx>=0 and (i-idx)<=k:
                return True
            numdict[nums[i]]=i
        return False
        