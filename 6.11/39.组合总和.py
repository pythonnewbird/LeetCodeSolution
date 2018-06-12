class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(candidates)==0:return []
        res=[]
        candidates=sorted(candidates)
        self.dfs(candidates,target,0,[],res)
        return res
    def dfs(self,nums,target,index,path,res):
        if target==0:
            res.append(path)
        for i in range(index,len(nums)):
            if target<nums[i]:
                break
            self.dfs(nums,target-nums[i],i,path+[nums[i]],res)