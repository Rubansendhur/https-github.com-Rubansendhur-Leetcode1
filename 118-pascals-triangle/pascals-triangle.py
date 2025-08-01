class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        
        res = [[1], [1,1]]
        

        for i in range(2 , numRows):
            c = res[i-1]
            sum_track = [] 
            for j in range(1,len(c)):
               sum_track.append(c[j-1] + c[j])
            res.append([1, *sum_track, 1])   

        return res
        
  
