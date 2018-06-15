class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        dic={}
        for ele in nums:
            if ele not in dic:
                dic[ele]=0
            dic[ele]+=1
        
        if 0 in dic and dic[0]>2:
            rst=[[0,0,0]]
        else:
            rst=[]
        pos=[p for p in dic if p>0]
        neg=[n for n in dic if n<0]
        for p in pos:
            for n in neg:
                reverse=-(p+n)
                if reverse in dic:
                    if reverse==p and dic[p]>1:
                        rst.append([n,p,p])
                    elif reverse==n and dic[n]>1:
                        rst.append([n,n,p])
                    elif reverse<n or reverse>p  or reverse==0:
                        rst.append([n,reverse,p])
        return rst