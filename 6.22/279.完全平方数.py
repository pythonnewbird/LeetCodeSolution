def dp(n):
            if n in d:
                return d[n]
            if math.sqrt(n)==int(math.sqrt(n)):
                d[n]=1
                return 1
            bound=int(math.sqrt(n))
            an=float('inf')
            for i in range(bound,bound//2,-1):
                an=min(an,dp(n-i*i)+1)
                
            d[n]=an
            return an
        return dp(n)
#递归