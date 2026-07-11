class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = [0]*len(nums)
        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if i != j:
                    prod *= nums[j]
            results[i] = prod
        return results