import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        [3,2,1,5,6,4], k = 2
        heapify
        [1,2,3,4,5,6]
        pop (n-k) times  (6-2) = 4 
        len(n) > k
        [1,2,3,4]
        """
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]

        



        