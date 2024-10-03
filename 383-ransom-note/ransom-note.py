class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magzine_count =  defaultdict(int)

        for ch in magazine:
            # If ch is present in hashmap
            if ch in magzine_count:
                magzine_count[ch] += 1
            #If ch is not present in hashmap
            else:
                magzine_count[ch] = 1
            
        for ch in ransomNote:
            if ch not in magzine_count:
                return False
            elif magzine_count[ch] == 1:
                del magzine_count[ch]
            else:
                magzine_count[ch] -=1
                
        return True
        