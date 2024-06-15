class NumArray:

    def __init__(self, nums: List[int]):
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i - 1]
        self.nums = nums
        print(nums)
        

    def sumRange(self, left: int, right: int) -> int:
        if left - 1 >= 0:
            return self.nums[right] - self.nums[left - 1]
        return self.nums[right]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)