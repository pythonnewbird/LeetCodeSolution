class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        cols=[set() for _ in range(9)]
        blks=[set() for _ in range(9)]
        for row in range(9):
            rows=set()
            for col in range(9):
                if board[row][col]!='.':
                    num=ord(board[row][col])-48
                    k=col/3*3+row/3
                    if num in rows or num in cols[col] or num in blks[k]:
                        return False
                    else:
                        rows.add(num)
                        cols[col].add(num)
                        blks[k].add(num)
        return True