class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        number_set = set()
        long_con_seq = 0
        for i in nums:
            number_set.add(i)
        for i in number_set:
            if (i - 1) in number_set:
                continue
            curr_num = i
            curr_count = 1
            while(curr_num + 1 in number_set):
                curr_num += 1
                curr_count += 1
            long_con_seq = max(curr_count, long_con_seq)
        return long_con_seq

            
        