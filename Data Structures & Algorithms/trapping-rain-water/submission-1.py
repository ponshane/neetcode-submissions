class Solution:
    def trap(self, height: List[int]) -> int:
        
        prefix_max_hight = [0] * len(height)
        for i in range(1, len(height)):
            prefix_max_hight[i] = max(height[:i])

        suffix_max_hight = [0] * len(height)
        for i in range(len(height)-2, -1, -1):
            suffix_max_hight[i] = max(height[i+1:])
        
        total_area = 0
        for i in range(1, len(height)-1):
            total_area += max(min(prefix_max_hight[i], suffix_max_hight[i]) - height[i],0)
        return total_area
        

