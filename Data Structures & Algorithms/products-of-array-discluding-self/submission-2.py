class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefixProd = [1] * len(nums)
        for i in range(1, len(nums)):
            prefixProd[i] = prefixProd[i-1] * nums[i-1]

        suffixProd = [1] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            suffixProd[i] = suffixProd[i+1] * nums[i+1]

        results = [0] * len(nums)
        for i in range(len(nums)):
            results[i] = prefixProd[i] * suffixProd[i]
        
        return results