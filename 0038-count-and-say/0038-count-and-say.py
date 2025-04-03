class Solution:
    def countAndSay(self, n: int) -> str:
        
     result = '1'

     for i in range(n-1):
        prev_char = result[0]
        current_char = ''
        count = 1

        for j in range(1 , len(result)):
            if result[j] == prev_char:
                count += 1
            else:
                current_char += str(count) + prev_char
                prev_char = result[j]
                count = 1
            
        current_char +=  str(count) + prev_char
        result = current_char

     return result










        


        
                

