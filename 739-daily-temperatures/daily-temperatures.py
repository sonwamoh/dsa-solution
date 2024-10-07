class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        res = [0] * len(temperatures)
        for i, tmp in enumerate(temperatures):
            while stk and tmp > stk[-1][1]:
                curr = stk.pop()
                res[curr[0]] = i - curr[0]
            stk.append([i, tmp])
        return res
        