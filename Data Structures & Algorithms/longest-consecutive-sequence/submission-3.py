class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
        
        seen = set()
        for num in nums:
            seen.add(num)
        
        start_candidates = set()
        for num in seen:
            if (num-1) not in seen:
                start_candidates.add(num)
        
        longest = 1
        for num in start_candidates:
            i = 1
            while (num+i) in seen:
                i += 1
                length = i
                if length > longest:
                    longest = length

        return longest
