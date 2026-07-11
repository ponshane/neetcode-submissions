class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n = len(s)
        l = 0
        # characters in the current window
        currentChars = set()
        max_length = 0

        for r in range(n):
            
            # s[r] in currentChars then we try to reduce windows
            while s[r] in currentChars:
                currentChars.remove(s[l])
                l += 1

            # s[r] not in currentChars
            currentChars.add(s[r])
            max_length = max(max_length, len(currentChars))

        return max_length         