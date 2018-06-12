class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        k-=1
        vals=[str(i) for i in range(1,n+1)]
        ans=''
        while vals!=[]:
            f=math.factorial(n-1)
            idx=k/f
            r=k%f
            ans+=vals[idx]
            del vals[idx]
            k=r
            n-=1
        return ans