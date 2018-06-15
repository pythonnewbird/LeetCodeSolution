class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        n=len(nums)
        if n==0:
            return False
        l,r=0,n-1
        while l<=r:
            mid=(l+r)/2
            if nums[mid]==target:
                return True
            #关键部分
            while l<mid and nums[l]==nums[mid]:
                l+=1
            while r>mid and nums[r]==nums[mid]:
                r-=1
            if nums[mid]>=nums[l]:
                if target>=nums[l] and target<nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
            else:
                if target<=nums[r] and target>nums[mid]:
                    l=mid+1
                else:
                    r=mid-1
        return False
