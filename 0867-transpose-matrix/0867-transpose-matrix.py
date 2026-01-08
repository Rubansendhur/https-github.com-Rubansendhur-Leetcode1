class Solution:
    def transpose(self, mat: List[List[int]]) -> List[List[int]]:
        
        m = len(mat)
        n = len(mat[0])

        res = [[0] * len(mat) for _ in range(len(mat[0]))]

        for i in range(m):
            for j in range(n):
                res[j][i] = mat[i][j]
        
        return res