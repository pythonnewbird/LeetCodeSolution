class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n=len(nums)
        max_index=n-1
        for i in range(n-2,-1,-1):
            if i+nums[i]>=max_index:
                max_index=i
        return max_index==0