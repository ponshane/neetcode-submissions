class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        index_last_char = {}
        l = 0
        max_length = 0

        for r in range(n):
            if s[r] in index_last_char:
                # Jump 'l' to the right of the previous occurrence
                # We use max() to ensure 'l' never moves backward
                l = max(l, index_last_char[s[r]]+1)

            index_last_char[s[r]] = r
            max_length = max(max_length, r-l+1)
            
        return max_length

