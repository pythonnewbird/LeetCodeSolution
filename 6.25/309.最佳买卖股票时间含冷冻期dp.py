class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        size=len(prices)
        if not size:
            return 0
        sell=[None]*size
        buy=[None]*size
        sell[0]=0
        buy[0]=-prices[0]
        for i in range(1,size):
            sell[i]=max(buy[i-1]+prices[i],sell[i-1]-prices[i-1]+prices[i])
            buy[i]=max(sell[i-2]-prices[i] if i>1 else None,buy[i-1]+prices[i-1]-prices[i])
        return max(sell)