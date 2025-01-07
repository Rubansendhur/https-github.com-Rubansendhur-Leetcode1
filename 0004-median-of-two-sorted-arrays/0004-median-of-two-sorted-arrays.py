class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        result = nums1 + nums2
        result.sort()
        n = len(result)

        if len(result) % 2 != 0:
            med = n // 2
            return float(result[med])
        else:
            med = n // 2
            med1 = med - 1
            ans = (result[med] + result[med1]) / 2.0
            return (ans)


        