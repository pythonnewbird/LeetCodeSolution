class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        dx = (1, 1, 1, 0, 0, -1, -1, -1)
        dy = (1, 0, -1, 1, -1, 1, 0, -1)
        for x in range(len(board)):
            for y in range(len(board[0])):
                lives = 0
                for z in range(8):
                    nx, ny = x + dx[z], y + dy[z]
                    lives += self.getCellStatus(board, nx, ny)
				#keys
                if lives + board[x][y] == 3 or lives == 3:
                    board[x][y] |= 2
        for x in range(len(board)):
            for y in range(len(board[0])):
                board[x][y] >>= 1
    def getCellStatus(self, board, x, y):
        if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
            return 0
        return board[x][y] & 1