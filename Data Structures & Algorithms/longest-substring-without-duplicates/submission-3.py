class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n = len(s)

        length_longest_substring = 0
        
        for i in range(n):
            seen = set()       
            for j in range(i, n):
                if s[j] not in seen:
                    seen.add(s[j])
                else:
                    break
            length_longest_substring = max(length_longest_substring, len(seen))
        
        return length_longest_substring