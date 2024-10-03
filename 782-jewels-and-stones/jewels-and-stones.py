class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = set()
        for jewel in jewels:
            jewel_set.add(jewel)
        print(jewel_set)
        number_of_jewel = 0
        for stone in stones:
            if stone in jewel_set:
                number_of_jewel += 1
        return number_of_jewel

        #TC: O(n)
        #SC : O(n)