class Solution:
    def addBinary(self, f_a: str, f_b: str) -> str:

        a = int(f_a)
        b = int(f_b)
        res = ''
        carry = 0

        if a == 0 and b == 0:
            return "0"

        while a or b or carry:

            a_bit = a % 10
            b_bit = b % 10

            total = a_bit + b_bit + carry

            if total == 0:
                res = '0' + res
                carry = 0

            if total == 1:
                res = '1' + res
                carry = 0

            if total == 2:
                res = '0' + res
                carry = 1

            if total == 3:
                res = '1' + res
                carry = 1
            
            a //= 10
            b //= 10
        

        return res
            
        