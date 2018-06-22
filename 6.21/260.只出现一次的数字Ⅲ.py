class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor=reduce(lambda x,y:x^y,nums)
        flag=xor&-xor
        a,b=0,0
        for num in nums:
            if num&flag:
                a^=num
            else:
                b^=num
        return [a,b]