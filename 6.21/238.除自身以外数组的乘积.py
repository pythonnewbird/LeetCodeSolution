class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        size=len(nums)
        ans=[1]*size
        left=1
        for i in range(size-1):
            left*=nums[i]
            ans[i+1]*=left
        right=1
        for i in range(size-1,0,-1):
            right*=nums[i]
            ans[i-1]*=right
        return ans