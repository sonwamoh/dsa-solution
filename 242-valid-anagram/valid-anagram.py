class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Optimize for space 
        TC: O(n)
        SC: O(1)
        """
        return sorted(s) == sorted(t)
        