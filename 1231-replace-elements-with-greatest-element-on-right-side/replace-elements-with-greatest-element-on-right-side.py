class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        prev_max = -1
        for i in range(len(arr) - 1, -1, -1):
            new_max = max(prev_max, arr[i])
            arr[i] = prev_max
            prev_max = new_max
        return arr