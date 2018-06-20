class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        return self.search(nums, 0, size - 1)
    
    def search(self, num, start, end):
        if start == end:
            return start
        if start + 1 == end:
            return [start, end][num[start] < num[end]]
        mid = (start + end) / 2
        if num[mid] < num[mid - 1]:
            return self.search(num, start, mid - 1)
        if num[mid] < num[mid + 1]:
            return self.search(num, mid + 1, end)
        return mid
