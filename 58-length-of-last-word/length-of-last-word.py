class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i, len_last_word = len(s) - 1, 0
        while s[i] == " ":
            i -= 1
        while i >= 0 and s[i] != " ":
            len_last_word += 1
            i -= 1
        return len_last_word

        