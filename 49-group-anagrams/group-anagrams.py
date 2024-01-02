class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        aet -> eat, tea, ate
        ant -> nat, tan
        abt -> bat
        """
        map = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key in map:
                map[key].append(s)
            else:
                map[key] = [s]
        res = []
        for i in map.values():
            res.append(i)
        return res
