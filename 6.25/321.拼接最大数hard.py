class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        def getmax(nums,t):
            ans=[]
            size=len(nums)
            for x in range(size):
                while ans and len(ans)+size-x>t and ans[-1]<nums[x]:
                    ans.pop()
                if len(ans)<t:
                    ans.append(nums[x])
            return ans
        def merge(nums1,nums2):
            return [max(nums1,nums2).pop(0) for _ in nums1+nums2]
        len1,len2=len(nums1),len(nums2)
        res=[]
        for x in range(max(0,k-len2),min(k,len1)+1):
            tmp=merge(getmax(nums1,x),getmax(nums2,k-x))
            res=max(res,tmp)
        return res