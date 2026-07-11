class Solution:
    def trap(self, height: List[int]) -> int:
        
        prefix_max_height = [0] * len(height)
        prefix_max_height[0] = height[0]
        
        for i in range(1, len(height)):
            # slicing raises n operation making it O(n^2)
            # prefix_max_height[i] = max(height[:i])
            prefix_max_height[i] = max(prefix_max_height[i-1], height[i])

        suffix_max_height = [0] * len(height)
        suffix_max_height[len(height)-1] = height[len(height)-1]
        for i in range(len(height)-2, -1, -1):
            suffix_max_height[i] = max(height[i], suffix_max_height[i+1])
        
        total_area = 0
        for i in range(1, len(height)-1):
            total_area += min(prefix_max_height[i], suffix_max_height[i]) - height[i]
        return total_area
        

