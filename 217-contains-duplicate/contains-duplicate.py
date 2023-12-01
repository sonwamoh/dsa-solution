class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        TC: O(n)
        SC: O(n)
        """
        if len(nums) == 0:
            return False
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False


        