class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        size=len(ratings)
        nums=[1]*size
        for i in range(1,size):
            if ratings[i]>ratings[i-1]:
                nums[i]=nums[i-1]+1
        for i in range(size-1,0,-1):
            if ratings[i]<ratings[i-1]:
                nums[i-1]=max(nums[i-1],nums[i]+1)
        return sum(nums)
贪心算法（Greedy Algorithm）

评分同时低于左右两边的孩子只需分配一个糖果

评分相同的相邻孩子，分配的糖果可以不同

算法步骤如下：

1. 首先为每一个孩子分配1个糖果

记当前孩子序号为i，糖果数为candies[i]，评分为ratings[i]

2. 从左向右遍历，若ratings[i] > ratings[i - 1]，则令candies[i] = candies[i - 1] + 1

3. 从右向左遍历，若ratings[x] > ratings[x + 1]，则令candies[x] = max(candies[x], candies[x + 1] + 1)