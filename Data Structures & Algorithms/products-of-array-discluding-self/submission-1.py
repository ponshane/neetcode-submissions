class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]*len(nums)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        suffix = [1]*len(nums)
        for i in range(len(nums)-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        
        results = [0] * len(nums)
        for i in range(len(nums)):
            results[i] = prefix[i]*suffix[i]
        
        return results
        """
        results = [0]*len(nums)
        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if i != j:
                    prod *= nums[j]
            results[i] = prod
        return results
        """