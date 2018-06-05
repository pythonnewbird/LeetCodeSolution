class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        d={}
        for idx,num in enumerate(numbers):
            if (target-num) in d:
                return [d[target-num]+1,idx+1]
            d[num]=idx