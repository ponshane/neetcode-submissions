class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0

        for num in nums:
            # only start with those stating numbers
            if num-1 not in nums:
                i = 1
                while (num+i) in nums:
                    i += 1
                longest = max(i, longest)
        
        return longest
                     
