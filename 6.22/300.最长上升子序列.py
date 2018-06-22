#O(n * log n)解法：维护一个单调序列，遍历nums数组，二分查找每一个数在单调序列中的位置，然后替换之。
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        dp = []
        for x in range(size):
            low, high = 0, len(dp) - 1
            while low <= high:
                mid = (low + high) / 2
                if dp[mid] >nums[x]:
                    high = mid - 1
                elif dp[mid]==nums[x]:
                    low=mid
                    break
                else:
                    low = mid + 1
            if low >= len(dp):
                dp.append(nums[x])
            else:
                dp[low] = nums[x]
        return len(dp)