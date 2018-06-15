class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        top=left=0
        bottom=len(matrix)-1
        right=len(matrix[0])-1
        res=[]
        direct=0
        while (top<=bottom and left<=right):
            if direct==0:
                for i in range(left,right+1):
                    res.append(matrix[top][i])
                top+=1
            if direct==1:
                for i in range(top,bottom+1):
                    res.append(matrix[i][right])
                right-=1
            if direct==2:
                for i in range(right,left-1,-1):
                    res.append(matrix[bottom][i])
                bottom-=1
            if direct==3:
                for i in range(bottom,top-1,-1):
                    res.append(matrix[i][left])
                left+=1
            direct=(direct+1)%4
        return res
        
