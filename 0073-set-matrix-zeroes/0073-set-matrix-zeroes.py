class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        zero_rows = []
        zero_cols = []
        
        # Step 1: Identify rows and columns to zero
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_rows.append(i)
                    zero_cols.append(j)

        # Step 2: Zero out identified rows and columns
        for i in range(m):
            for j in range(n):
                if i in zero_rows or j in zero_cols:
                    matrix[i][j] = 0
        
