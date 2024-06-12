class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                prev_temp, prev_index = stack.pop()
                res[prev_index] = i - prev_index 
            stack.append((temp, i))
        return res


        
            

        