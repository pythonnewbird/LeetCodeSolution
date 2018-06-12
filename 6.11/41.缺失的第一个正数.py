class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
		#加入0
        nums.append(0)
        n=len(nums)
        for i in range(len(nums)):
			#等号不能少，不然hash的时候1，n的效果一样
            if nums[i]<0 or nums[i]>=n:
                nums[i]=0
        for num in nums:
            nums[num%n]+=n
        i=0
        while i<n and nums[i]>=n:
            i+=1
        return i