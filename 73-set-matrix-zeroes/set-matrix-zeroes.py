class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        zero_rows = set()
        zero_cols = set()

        for rows in range(m):
            for cols in range(n):
                if matrix[rows][cols] == 0:
                    zero_rows.add(rows)
                    zero_cols.add(cols)
        
        for rows in range(m):
            for cols in range(n):
                if rows in zero_rows or cols in zero_cols:
                    matrix[rows][cols] = 0
