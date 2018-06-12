class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[[]]
        for num in nums:
            new_res=[]
            for perm in res:
                
                for i in xrange(len(perm)+1):
                    new_res.append(perm[:i]+[num]+perm[i:])
	    #去除重复的排列
                    if i<len(perm) and perm[i]==num:
                        break
            res=new_res
        return res