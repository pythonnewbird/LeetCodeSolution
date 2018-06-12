class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length=len(nums)
        if length<=3:
            return sum(nums)
        else:
            nums=sorted(nums)
            minSum=nums[0]+nums[1]+nums[2]
            if minSum>target:
                return minSum
            maxSum=nums[-1]+nums[-2]+nums[-3]
            if maxSum<=target:
                return maxSum
            
            if target-minSum<maxSum-target:
                closest=minSum
                distance=target-minSum
            else:
                closest=maxSum
                distance=maxSum-target
            for i in xrange(length-2):
                if i>0 and nums[i]==nums[i-1]:
                    continue
                left=i+1
                right=length-1
                while left<right:
                    s=nums[i]+nums[left]+nums[right]
                    dis=abs(target-s)
                    
                    if dis<distance:
                        closest=s
                        distance=dis
                    
                    if s==target:
                        return closest
                    elif s<target:
                        
                        left+=1
                    else:
                        
                        right-=1
        return closest
        