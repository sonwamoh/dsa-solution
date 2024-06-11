class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        solving using counting sort
        """
        nums_len = len(nums)
        nums += [0,0,0]
        print(nums)
        for i in range(nums_len):
            print(nums[i])
            if nums[i] == 0:
                nums[nums_len] += 1
            elif nums[i] == 1:
                nums[nums_len + 1] += 1
            elif nums[i] == 2:
                nums[nums_len + 2] += 1
        k = 0
        for i in range(0,3):
            count_index = nums_len + i
            for j in range(0, nums[count_index]):
                nums[k] = i
                k += 1
        for _ in range(3):
            nums.pop()

        