class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        vmap = collections.defaultdict(set)
        M, N = len(matrix), len(matrix[0])
        for x in range(M):
            for y in range(N):
                vmap[y - x].add(matrix[x][y])
                if len(vmap[y - x]) > 1: return False
        return True