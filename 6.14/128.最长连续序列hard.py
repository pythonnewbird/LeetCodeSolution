class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        nums=set(nums)
        ans=1
        for num in nums:
            if num-1 not in nums:
                
                y=num+1
                while y in nums:
                    y+=1
                ans=max(ans,y-num)
        return ans
#O(n)            