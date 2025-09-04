class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:

        stepx = abs(x-z)
        stepy = abs(y-z)

        if stepx > stepy:
            return 2
        elif stepx < stepy :
            return 1
        else:
            return 0