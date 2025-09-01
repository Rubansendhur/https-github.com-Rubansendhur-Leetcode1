class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        """
        conditions 
            1) any 1 with less than 2 living(1) neighbour dies
            2) any 1 with 2 or 3 (1) neighbours lives on to the next generation
            3) any 1 with more than 3 (1) neighbour dies
            4) any dead(0) with exactly 3 live neighbours live

        """

        possible_dir = [(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1)]


        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                live = 0
                for x,y in possible_dir:
                    if (i+x < m and i+x >= 0) and (j+y < n and j+y>=0) and abs(board[i+x][j+y])==1:
                        live += 1

                if board[i][j]==1 and (live<2 or live>3):    
                        board[i][j] = -1
                if board[i][j]==0 and live==3:                  
                        board[i][j] = 2
        
        for i in range(m):
            for j in range(n):
                board[i][j] =1 if(board[i][j] > 0) else 0
