class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums)==0:
            return [-1,-1]
        i=0
        j=len(nums)-1
        #使用i<j-1是为了防止无限循环
        while i<j-1:
            mid=(i+j)/2
            if nums[mid]>=target:
                j=mid
            elif nums[mid]<target:
                i=mid
        #nums[0]==target的情况
        if nums[i]==target:
            left=i
        elif nums[j]==target:
            left=j
        else:
            left=-1
        i=0
        j=len(nums)-1
        while i<j-1:
            mid=(i+j)/2
            if nums[mid]<=target:
                i=mid
            elif nums[mid]>target:
                j=mid
        if nums[j]==target:
            right=j
        elif nums[i]==target:
            right=i
        else:
            right=-1
        return [left,right]