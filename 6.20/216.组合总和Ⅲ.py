class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        ans=[]
        def find(start,cnt,sums,nums):
            if cnt>k or sums>n:
                return
            if cnt==k and sums==n:
                ans.append(nums)
                return
            for i in range(start+1,10):
                find(i,cnt+1,sums+i,nums+[i])
        find(0,0,0,[])
        return ans