class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        buy=prices[0]
        res=0
        for p in prices:
            if p>buy:
                res=max(res,p-buy)
            else:
                buy=p
        return res