class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not len(board):
            return
        m,n=len(board),len(board[0])
        queue=set([(i,j) for i in (0,m-1) for j in range(n) if board[i][j]=='O']+[(i,j) for i in range(m) for j in (0,n-1) if board[i][j]=='O'])
        while queue:
            x,y=queue.pop()
            board[x][y]='S'
            for dx,dy in zip([0,1,0,-1],[1,0,-1,0]):
                nx,ny=x+dx,y+dy
                if 0<=nx and nx<m and 0<=ny and ny<n and board[nx][ny]=='O':
                    queue.add((nx,ny))
                    board[nx][ny]='S'
        board[:]=[['XO'[c=='S'] for c in row ] for row in board]