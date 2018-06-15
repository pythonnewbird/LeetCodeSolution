class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        else:
            start=0
            end=len(nums)-1
            while (start<=end):
                mid=(start+end)/2
                if nums[mid]==target:
                    return mid
                else:
                    if nums[start]<=nums[mid]:
                        if target<nums[mid] and target>=nums[start]:
                            end=mid-1
                        else:
                            start=mid+1
                    elif nums[mid]<nums[end]:
                        if target>nums[mid] and target<=nums[end]:
                            start=mid+1
                        else:
                            end=mid-1
            return -1