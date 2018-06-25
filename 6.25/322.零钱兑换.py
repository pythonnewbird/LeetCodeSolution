class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [0] + [-1] * amount
        for x in range(amount):
            if dp[x] < 0:
                continue
            for c in coins:
                if x + c > amount:
                    continue
                if dp[x + c] < 0 or dp[x + c] > dp[x] + 1:
                    dp[x + c] = dp[x] + 1
        return dp[amount]
		
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        steps = collections.defaultdict(int)
        queue = collections.deque([0])
        steps[0] = 0
        while queue:
            front = queue.popleft()
            level = steps[front]
            if front == amount:
                return level
            for c in coins:
                if front + c > amount:
                    continue
                if front + c not in steps:
                    queue += front + c,
                    steps[front + c] = level + 1
        return -1