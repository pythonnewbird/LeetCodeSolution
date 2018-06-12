class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        i,j=n-1,n-1
        while i>0 and nums[i]<=nums[i-1]:
            i-=1
        if i==0:
            nums[:]=nums[::-1]
            return
        #找下一个更大的数
        for j in range(n-1,i-2,-1):
            if nums[j]>nums[i-1]:
                break
        nums[i-1],nums[j]=nums[j],nums[i-1]
        nums[i:]=nums[i:][::-1]