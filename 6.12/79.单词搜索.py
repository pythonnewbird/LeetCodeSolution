import collections
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def precheck(board,word):
            cb=collections.defaultdict(int)
            cw=collections.defaultdict(int)
            for i in range(m):
                for j in range(n):
                    cb[board[i][j]]+=1
            for c in word:
                cw[c]+=1
            for c in cw:
                if (c not in cb) or cw[c]>cb[c]:
                    return False
            return True
        def dfs(x,y,p):
            val=board[x][y]
            if val!=word[p]:
                return False
            if p==len(word)-1:
                return True
            board[x][y]='#'
            for dx,dy in zip([1,0,-1,0],[0,1,0,-1]):
                nx,ny=x+dx,y+dy
                if 0<=nx and nx<m and 0<=ny and ny<n:
                    if dfs(nx,ny,p+1):
                        return True
            board[x][y]=val
            return False
        
        
        m,n=len(board),len(board[0])
        if m==0:
            return False
        if not precheck(board,word):
            return False
        for i in range(m):
            for j in range(n):
                if dfs(i,j,0):
                    return True
        return False
            
