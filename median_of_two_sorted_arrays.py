class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        sorted_array = sorted(nums1 + nums2)
        n = len(sorted_array)
        n2 = n+1
        print(f"{sorted_array = }")
        if n%2 == 0:
            median = (((sorted_array[n//2])-1) + ((sorted_array[(n//2)+1])-1)) / 2
        else:
            median = sorted_array[(n2//2)-1]

        return float(median)

s = Solution()
print(s.findMedianSortedArrays([1,3], [2]))
n1 = [1,2]
n2 = [3,4]
print(s.findMedianSortedArrays(n1, n2))
