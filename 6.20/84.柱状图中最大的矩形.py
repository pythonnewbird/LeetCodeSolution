class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack=[-1]
        ans=0
        size=len(heights)
        heights.append(0)
        for i in range(size+1):
            while heights[i]<heights[stack[-1]]:
                h=heights[stack.pop()]
                w=i-stack[-1]-1
                area=h*w
                if area>ans:
                    ans=area
            stack.append(i)
        return ans