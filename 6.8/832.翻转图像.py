class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for row in A:
            i, j = 0, len(row)-1
            while i <= j:
                row[i], row[j] = 1 if row[j]==0 else 0, 1 if row[i]==0 else 0
                i, j = i+1, j-1
        return A 