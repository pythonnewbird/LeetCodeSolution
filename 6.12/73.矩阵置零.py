class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row_len=len(matrix[0])
        set_r=[]
        set_c=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    set_r.append(i)
                    set_c.append(j)
        for x in set_r:
            matrix[x]=[0]*row_len
        for c in set_c:
            for i in range(len(matrix)):
                matrix[i][c]=0