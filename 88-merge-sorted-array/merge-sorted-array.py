class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        curr = m + n - 1
        first = m - 1
        second = n - 1
        while first >=0 and second >= 0:
            if nums1[first] > nums2[second]:
                nums1[curr] = nums1[first]
                first -= 1
            else:
                nums1[curr] = nums2[second]
                second -= 1
            curr -= 1
        
        print(nums1)

        while curr >= 0 and first >= 0:
            nums1[curr] = nums1[first]
            first -= 1
            curr -= 1

        while curr >= 0 and second >= 0:
            nums1[curr] = nums2[second]
            second -= 1
            curr -= 1

        print(nums1)

