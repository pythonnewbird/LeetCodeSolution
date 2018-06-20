class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        x,size=0,len(nums)
        ans=[]
        while x<size:
            r,c=x,str(nums[x])
            while x+1<size and nums[x+1]-nums[x]==1:
                x+=1
            if x>r:
                ans.append(c+'->'+str(nums[x]))
            else:
                ans.append(c)
            x+=1
        return ans