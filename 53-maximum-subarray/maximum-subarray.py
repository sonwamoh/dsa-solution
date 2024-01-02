class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_subarray = float('-inf')
        cur_sum = 0
        for n in nums:
            cur_sum += n
            max_subarray = max(cur_sum, max_subarray)
            if cur_sum < 0:
                cur_sum = 0
        return max_subarray
            

            
