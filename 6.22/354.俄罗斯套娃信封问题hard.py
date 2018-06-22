class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        nums=sorted(envelopes,cmp=lambda x,y: x[0]-y[0] if x[0]!=y[0] else y[1]-x[1])
        dp=[]
        
        for x in range(len(nums)):
            low=0
            high=len(dp)-1
            while low<=high:
                mid=(low+high)/2
                if dp[mid][1]<nums[x][1]:
                    low=mid+1
                elif dp[mid][1]==nums[x][1]:
                    low=mid
                    break
                else:
                    high=mid-1
            if low>=len(dp):
                dp.append(nums[x])
            else:
                dp[low]=nums[x]
        return len(dp)