class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        param: list on int
        return: list of triplets
        logic:
        nums[i] + nums[j] + nums[k] == 0
        i != j, i != k, and j != k
        output must not contain duplicate triplets
        """
        """
        Simulation 
        [-1,0,1,2,-1,-4]
        sort the list: O(nlogn)
        [-4,-1,-1,0,1,2]
        avoid positives: iterate only till 2nd index 
        skip elements if its same as previous element
        """
        res = []
        nums.sort()
        for index in range(len(nums)):
            if nums[index] > 0:
                continue
            if index > 0 and nums[index] == nums[index - 1]:
                continue
            left = index + 1
            right = len(nums) - 1
            while left < right:
                curr_sum = nums[index] + nums[left] + nums[right]
                if curr_sum == 0:
                    res.append([nums[index], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1 
                if curr_sum > 0:
                    right -= 1
                if curr_sum < 0:
                    left += 1
            
        return res
                
            
                