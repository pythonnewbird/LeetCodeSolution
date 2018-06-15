class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[[]]
        for num in nums:
            new_res=[]
            for perm in res:
                n=len(perm)
                for i in range(n+1):
                    new_res.append(perm[:i]+[num]+perm[i:])
            res=new_res
        return res
		
		
#BFS