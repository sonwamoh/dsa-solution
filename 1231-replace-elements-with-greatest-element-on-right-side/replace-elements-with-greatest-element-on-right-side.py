class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return [-1]
        next_great = arr[len(arr) - 1]
        for i in range(len(arr) - 2, -1, -1):
            curr_great = next_great
            if arr[i] > curr_great:
                next_great = arr[i]
            arr[i] = curr_great
        arr[len(arr) - 1] = -1
        return arr

            

        