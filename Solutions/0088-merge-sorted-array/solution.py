class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = m - 1
        j = n - 1
        e = m + n - 1

        while j >= 0:
            if i < 0:
                nums1[j] = nums2[j]
                j -= 1
                continue

            if nums2[j] >= nums1[i]:
                nums1[e] = nums2[j]
                j -= 1
            else:
                nums1[e] = nums1[i]
                i -= 1
            e -= 1
