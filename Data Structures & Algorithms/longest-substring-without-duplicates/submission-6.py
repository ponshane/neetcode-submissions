class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seenChars = set()
        maxLength = 0
        l, r = 0, 0
        while r < len(s):
            if s[r] not in seenChars:
                seenChars.add(s[r])
                maxLength = max(maxLength, r - l + 1)
                r += 1
            else:
                seenChars.remove(s[l])
                l += 1
        return maxLength
        