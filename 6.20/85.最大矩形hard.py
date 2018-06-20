class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix)==0 or len(matrix[0])==0:
            return 0
        n=len(matrix[0])
        height=[0]*(n+1)
        ans=0
        for row in matrix:
            for i in range(n):
                if row[i]=='1':
                    height[i]=height[i]+1
                else:
                    height[i]=0
            stack=[-1]
            for i in range(n+1):
                while height[stack[-1]]>height[i]:
                    h=height[stack.pop()]
                    w=i-stack[-1]-1
                    area=h*w
                    if area>ans:
                        ans=area
                stack.append(i)
        return ans