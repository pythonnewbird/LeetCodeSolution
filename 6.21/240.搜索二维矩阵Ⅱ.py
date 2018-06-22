class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not len(matrix) or len(matrix[0])==0: return False
        y = len(matrix[0]) - 1
        for x in range(len(matrix)):
            while y and matrix[x][y] > target:
                y -= 1
            if matrix[x][y] == target:
                return True
        return False