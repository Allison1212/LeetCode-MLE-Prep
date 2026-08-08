class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])
        

        # orginal  new   simble 
        #   0       0       0
        #   1       1       1
        #   0       1       2
        #   1       0       3

        def count_nei(x,y):
            nei = 0
            for i in range(x-1,x+2):
                for j in range(y-1,y+2):
                    if i < 0 or j < 0 or i >row-1 or j >col-1 or (i ==x and j == y):
                        continue
                    else:
                        if board[i][j] == 1 or board[i][j] == 3:
                            nei+=1
            return nei

        for x in range(row):
            for y in range(col):
                count = count_nei(x,y)
                if board[x][y] == 1:
                    if count > 3 or count < 2:
                        board[x][y] = 3
                else:
                    if count == 3:
                        board[x][y] = 2

        for x in range(row):
            for y in range(col):
                if board[x][y] == 2:
                    board[x][y] = 1
                if board[x][y] == 3:
                    board[x][y] = 0