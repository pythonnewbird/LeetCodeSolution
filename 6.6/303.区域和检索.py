class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        size = len(nums)
        self.sums = [0] * (size + 1)
        for x in range(size):
            self.sums[x + 1] += self.sums[x] + nums[x]
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sums[j + 1] - self.sums[i]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)