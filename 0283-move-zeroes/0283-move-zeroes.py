class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        non_zeros = 0
        arr = nums

        for i in range(len(nums)):
            if arr[i] != 0:
                arr[non_zeros] = arr[i]
                non_zeros += 1

        for i in range(non_zeros, len(nums)):
            arr[i] = 0

        return arr
        