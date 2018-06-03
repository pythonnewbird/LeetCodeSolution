class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen={}
        for i,n in enumerate(nums):
            if target-n in seen:
                return [seen[target-n],i]
            seen[n]=i

O(n) O(1)