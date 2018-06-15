class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def DFS(queens,xy_diff,xy_sum):
            p=len(queens)
            if p==n:
                ans.append(queens)
                return 
            #q表示新的皇后所在的列,p表示新的皇后所在的行
            for q in range(n):
                if q not in queens and p-q not in xy_diff and p+q not in xy_sum:
                    DFS(queens+[q],xy_diff+[p-q],xy_sum+[p+q])
        ans=[]
        DFS([],[],[])
        return [['.'*i+'Q'+'.'*(n-1-i) for i in sol] for sol in ans]
