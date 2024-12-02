class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return True

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:  # Check if the current spot is empty
                # Check left and right neighbors
                prev = (i == 0) or (flowerbed[i - 1] == 0)
                next = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)

                if prev and next:  # If both neighbors are empty
                    flowerbed[i] = 1  # Place a flower
                    n -= 1  # Decrease the count of flowers to place

                    if n == 0:  # If no more flowers need to be placed
                        return True

        return n == 0  # Check if all flowers were placed
