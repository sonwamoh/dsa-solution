class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxWater= 0
        l , r = 0, len(height) - 1
        while l < r:
            minBar = min(height[l], height[r])
            maxWater = max(maxWater, minBar * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxWater