class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        results = []
        nums = sorted(nums)

        for i in range(0, len(nums)-2):
            
            # don't start with the one with the same value we've processed
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i + 1
            r = len(nums) - 1
            
            while (l < r):
                if nums[l] + nums[r] > -nums[i]:
                    r -=1
                elif nums[l] + nums[r] < -nums[i]:
                    l +=1
                # find the answer
                elif nums[l] + nums[r] == -nums[i]:
                    
                    results.append([nums[i], nums[l], nums[r]])

                    # avoid the same value 
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1

                    l +=1
                    r -=1           

        return results
