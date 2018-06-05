class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        results=[True]*max(n,2)
        results[0],results[1]=False,False
        x=2
        while x*x<n:
            if results[x]:
                tmp=x*x
                while tmp<n:
                    results[tmp]=False
                    tmp+=x
            x+=1
        return sum(results)
        