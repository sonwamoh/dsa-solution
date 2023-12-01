class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Optimize for space 
        TC: O(n)
        SC: O(1)
        """
        if len(s) != len(t):
            return False
        s_count = {}
        t_count = {}
        for s1, t1 in zip(s, t):
            s_count[s1] = s_count.get(s1, 0) + 1
            t_count[t1] = t_count.get(t1, 0) + 1
        print(s_count, t_count)
        return s_count == t_count

        
        