class Solution:
    def isValid(self, s: str) -> bool:
        char_map = {')': '(', ']': '[', '}': '{'}
        stk = []
        for ch in s:
            if stk and ch in char_map:
                open_brc = char_map.get(ch)
                if open_brc != stk.pop():
                    return False
            else:
                stk.append(ch)
            
        return len(stk) == 0


        