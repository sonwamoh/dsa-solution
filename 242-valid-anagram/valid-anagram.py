class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Optimize for space 
        TC: O(n)
        SC: O(1)
        """
        return ''.join(sorted(s)) == ''.join(sorted(t))
        