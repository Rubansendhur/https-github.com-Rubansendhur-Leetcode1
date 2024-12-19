class Solution:
    def leftbs(self,target, arr):
        fin = -1
        i = 0 
        j = len(arr)-1

        while i <= j:
            mid = (i + j) // 2
    
            if arr[mid] == target:
                fin = mid
                j = mid - 1
            elif arr[mid] > target:
                j = mid - 1
            else:
                i = mid + 1
        return fin
                
    def rightbs(self,target, arr):
        fin = -1
        i = 0 
        j = len(arr)-1

        while i <= j:
            mid = (i + j) // 2
    
            if arr[mid] == target:
                fin = mid
                i = mid + 1
            elif arr[mid] > target:
                j = mid - 1
            else:
                i = mid + 1
        return fin

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = []
        
        ans.append(self.leftbs(target,nums))
        ans.append(self.rightbs(target,nums))

        return ans



        
        

        
        
        

        



        