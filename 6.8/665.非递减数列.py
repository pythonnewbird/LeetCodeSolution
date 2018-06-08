class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        modify=False
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                if modify:return False
                modify=True
                pre=nums[i-2] if i>1 else None
                if not pre:
                    nums[i-1]=nums[i]
                else:
                    if pre>nums[i]:
                        nums[i]=nums[i-1]
                    else:
                        nums[i-1]=nums[i-2]
        return True