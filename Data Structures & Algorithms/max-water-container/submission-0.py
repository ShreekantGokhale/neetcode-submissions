class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_a = 0
        while l<r:
            if heights[l] <= heights[r]:
                area = heights[l]*(r-l)
                l += 1
            else:
                area = heights[r]*(r-l)
                r -= 1
            max_a = max(area,max_a)
        return max_a

