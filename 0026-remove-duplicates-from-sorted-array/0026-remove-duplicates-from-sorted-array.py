class Solution:
    def removeDuplicates(self, a: List[int]) -> int:
        for i in range(len(a)):
            j = i + 1
            while j < len(a):  # Use while loop to handle shifting indices
                if a[i] == a[j]:
                    del a[j]  # Remove duplicate, but do not increment `j`
                else:
                    j += 1  # Increment `j` only if no removal

        k = len(a)
        return k
        