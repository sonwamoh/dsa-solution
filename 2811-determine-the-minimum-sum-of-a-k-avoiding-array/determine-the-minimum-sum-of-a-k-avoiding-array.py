class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        k_avoid_ele = set()
        res_size = 0
        res = 0
        for i in range(1, 1000000):
            if i not in k_avoid_ele:
                res += i
                res_size += 1
                k_avoid_ele.add(k - i)
            if res_size == n:
                return res
        return res
            



        