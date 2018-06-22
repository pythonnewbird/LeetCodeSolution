class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        if not num:
            return []
        if len(num) == 1:
            if int(num) == target:
                return [num]
            return []

        nums = [int(i) for i in num]
        res = []
        def dfs(i,expr,prod,prevSum,curr):
            if i == len(nums)-1:
                if prevSum + prod + nums[i] == target:
                    res.append(expr + '+' + str(nums[i]))
                if prevSum + prod - nums[i] == target:
                    res.append(expr + '-' + str(nums[i]))
                if prevSum + prod*nums[i] == target:
                    res.append(expr + '*' + str(nums[i]))
                
                if curr and 10*prod + prod//curr*nums[i] + prevSum == target:
                    res.append(expr+str(nums[i]))
            else:
                dfs(i+1, expr+'+'+str(nums[i]), nums[i], prod+prevSum, nums[i])
                dfs(i+1, expr+'-'+str(nums[i]), -nums[i], prod+prevSum, nums[i])
                dfs(i+1, expr+'*'+str(nums[i]), nums[i]*prod, prevSum, nums[i])
                if curr:
                    # append nums[i] directly to last number, impossible when last number is 0
                    #注意curr与prod的区别，prod带符号
                    dfs(i+1, expr+str(nums[i]), 10*prod + prod//curr*nums[i], prevSum, 10*curr+nums[i])
        
        dfs(1, str(nums[0]), nums[0], 0, nums[0])
        return res
            