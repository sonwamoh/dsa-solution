class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []
        for opr in operations:
                if opr == 'C':
                    stk.pop()
                elif opr == 'D':
                    curr = int(stk[-1])
                    stk.append(2 * curr)
                elif opr == '+':
                    curr_1, curr_2 = int(stk[-1]), int(stk[-2])
                    stk.append(curr_1 + curr_2)
                else:
                    stk.append(int(opr))
        return sum(stk)
        