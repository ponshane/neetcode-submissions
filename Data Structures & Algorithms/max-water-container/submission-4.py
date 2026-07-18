class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxValue = 0
        l, r = 0, len(heights) - 1

        while l < r:
            currentValue = (r - l) * min(heights[l], heights[r]) # width * height
            maxValue = max(maxValue, currentValue)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return maxValue
        