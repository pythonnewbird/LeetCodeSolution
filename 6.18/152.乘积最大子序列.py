class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=max(nums)
        size=len(nums)
        positive_max = [0 for x in range(size)]
        negative_min = [0 for x in range(size)]
        if nums[0] > 0:
            positive_max[0] =nums[0]
        elif nums[0] < 0:
            negative_min[0] = nums[0]
        for x in range(1, size):
            if nums[x] > 0:
                positive_max[x] = max(positive_max[x - 1] *nums[x], nums[x])
                negative_min[x] = negative_min[x - 1] * nums[x]
            elif nums[x] < 0:
                positive_max[x] = negative_min[x - 1] * nums[x]
                negative_min[x] = min(positive_max[x - 1] *nums[x], nums[x])
            if positive_max[x] and positive_max[x] > ans:
                ans = positive_max[x]
        return ans
