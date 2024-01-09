class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            sum = numbers[left] + numbers[right]
            if target == sum:
                return [left + 1, right + 1]
            if target > sum:
                left += 1
            if target < sum:
                right -= 1
        return []
"""
Lesson Learnt:
1. Be careful of equality logic
2. use fimilar pointer names
3. check what position of index you are suppose to return
"""