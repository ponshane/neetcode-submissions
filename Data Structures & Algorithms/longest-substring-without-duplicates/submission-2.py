class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n = len(s)

        if n == 1:
            return 1
            
        longest_substring = ""
        
        for i in range(n-1):         
            seen = set([s[i]])
            tmp_substring = s[i]
            for j in range(i+1, n):
                if s[j] not in seen:
                    seen.add(s[j])
                    tmp_substring = tmp_substring + s[j]
                else:
                    break
            if len(tmp_substring) > len(longest_substring):
                longest_substring = tmp_substring
        
        return len(longest_substring)