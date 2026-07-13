class Solution:
    # Kadane's variant algorithm
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = nums[0]
        CurrentMax = 1
        CurrentMin = 1

        for num in nums:
            
            temp = min(num, num*CurrentMax, num*CurrentMin)
            CurrentMax = max(num, num*CurrentMax, num*CurrentMin)
            CurrentMin = temp
            maxProd = max(maxProd, CurrentMax)

        return maxProd