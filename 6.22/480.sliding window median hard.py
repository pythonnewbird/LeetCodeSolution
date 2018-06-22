import bisect
class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        if k==0: return []
        ans=[]
        window=sorted(nums[:k])
        for i in range(k,len(nums)+1):
            ans.append((window[k/2]+window[(k-1)/2])/2.0)
            if i==len(nums): break
            index=bisect.bisect_left(window,nums[i-k])
            window.pop(index)
            bisect.insort_left(window,nums[i])
        return ans