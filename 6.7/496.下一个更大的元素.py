class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        dmap={}
        stack=[]
        for n in nums:
            while stack and stack[-1]<n:
                dmap[stack.pop()]=n
            stack.append(n)
        return [dmap.get(m,-1) for m in findNums]