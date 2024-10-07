class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                return m
        if nums[m] < target: return m + 1
        if target < nums[m]: return m 
        