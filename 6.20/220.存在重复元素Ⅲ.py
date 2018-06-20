class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k<1 or t<0:
            return False
        dic=collections.OrderedDict()
        for x in range(len(nums)):
            m=nums[x]/max(1,t)
            for i in (m-1,m,m+1):
                if i in dic and abs(nums[x]-dic[i])<=t:
                    return True
            dic[m]=nums[x]
            if x>=k:
                dic.popitem(last=False)
        return False