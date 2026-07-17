class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_dict = {num: True for num in nums}

        maxseqlength = 0
        for num in nums:
            # if num is the start of the seq
            if num - 1 not in num_dict:
                seqlength = 0
                tmp = num
                while tmp in num_dict:
                    seqlength += 1
                    maxseqlength = max(maxseqlength, seqlength)
                    tmp += 1
        return maxseqlength

        