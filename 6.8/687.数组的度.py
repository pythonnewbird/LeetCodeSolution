class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mins = {}
        maxs = {}
        cnts = collections.defaultdict(int)
        for idx, num in enumerate(nums):
            maxs[num] = max(maxs.get(num, -1), idx)
            mins[num] = min(mins.get(num, 0x7FFFFFFF), idx)
            cnts[num] += 1
        degree = max(cnts.values())
        ans = len(nums)
        for num in set(nums):
            if cnts[num] == degree:
                ans = min(ans, maxs[num] - mins[num] + 1)
        return ans