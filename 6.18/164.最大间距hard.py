import math
class Solution:
    # @param num, a list of integer
    # @return an integer
    def maximumGap(self, nums):
        N=lem(nums)
        if N<2:
            return 0
        A=min(nums)
        B=max(nums)
        bucketRange=max(1,int(math.ceil((B-A)/(N-1))))
        bucketLen=(B-A)/bucketRange+1
        buckets=[None]*bucketLen
        for K in nums:
            loc=(K-A)/bucketRange
            bucket=buckets[loc]
            if bucket is None:
                bucket={'min':K,'max':K}
                buckets[loc]=bucket
            else:
                buckets['min']=min(buckets['min'],K)
                buckets['max']=max(buckets['max'],K)
        maxGap=0
        for x in range(bucketLen):
            if buckets[x] is None:
                continue
            y=x+1
            while y<bucketLen and buckets[y] is None:
                y+=1
            if y<bucketLen:
                maxGap=max(maxGap,buckets[y]['min']-buckets[x]['max'])
            x=y
        return maxGap
        
