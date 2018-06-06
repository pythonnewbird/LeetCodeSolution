class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        return int(math.ceil(math.log(buckets, 1 + minutesToTest / minutesToDie)))
		
		
		
0 1 2 3 4 5 6 7 （组序号）
0 0 0 0 1 1 1 1 （第1头猪饮用：4，5，6，7）
0 0 1 1 0 0 1 1 （第2头猪饮用：2，3，6，7）
0 1 0 1 0 1 0 1 （第3头猪饮用：1，3，5，7）
8 4 4 2 4 2 2 1 （桶数量）

合计： 1 * 8 + 3 * 4 + 3 * 2 + 1 * 1 = 27

因此3头猪做2轮试验可以确定的最大桶数为pow(3, 3) = 27
pow(轮数+1，猪的数目)