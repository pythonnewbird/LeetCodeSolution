class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        h, w = len(nums), len(nums[0])
        if h * w != r * c: return nums
        ans = []
        for x in range(r):
            row = []
            for y in range(c):
                row.append(nums[(x * c + y) / w][(x * c + y) % w])
            ans.append(row)
        return ans