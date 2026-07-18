class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort() #in-place sorting O(nlogn)

        for i, num in enumerate(nums):
            # skip the same number for non-duplicate triplets
            if i > 0 and num == nums[i-1]:
                continue
            
            l, r = i+1, len(nums) - 1
            while l < r:
                currentSum = nums[i] + nums[l] + nums[r]
                if currentSum > 0:
                    r -= 1
                elif currentSum < 0:
                    l += 1
                else: # currentSum == 0
                    results.append([nums[i],nums[l],nums[r]]) # hit a valid triplet
                    # keep searching
                    l += 1
                    r -= 1

                    # avoid duplicate
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        
        return results