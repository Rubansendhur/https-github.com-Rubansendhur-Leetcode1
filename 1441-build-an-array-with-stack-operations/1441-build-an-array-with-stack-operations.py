class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        no = []

        # for i in range(1, n+1):
        #     res.append("Push")
        #     if res == target:
        #         break
        #     if i not in target:
        #         res.append("Pop")

        # return res

        i = 1
        while i < n + 1 and target != no:
            if target == no:
                break
            else:
                res.append("Push")
                no.append(i)
                
            if i not in target:
                res.append("Pop")
                no.pop()
            i += 1
        
        return res

            