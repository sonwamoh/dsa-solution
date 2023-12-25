class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ptr = len(s) - 1
        while(s[ptr] == ' '):
            ptr -= 1
        len_last_word = 0
        while(s[ptr] != ' ' and ptr >= 0):
            len_last_word += 1
            ptr -= 1
        return len_last_word