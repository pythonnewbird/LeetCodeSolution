class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) / 2
            if left+1==right:
                return min(nums[left],nums[right])
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                return min(self.findMin(nums[:mid+1]), self.findMin(nums[mid+1:]))
        return nums[left]
