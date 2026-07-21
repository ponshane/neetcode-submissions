class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLength = 0
        l, r = 0, 0
        count = [0] * 26 # initialize count array for 26 uppercase English characters

        while r < len(s):
            count[ord(s[r]) - ord("A")] += 1
            while (r-l+1) - max(count) > k:
                # shrink if there is no replacement budget
                count[ord(s[l]) - ord("A")] -= 1
                l += 1
            maxLength = max(maxLength, (r-l+1))
            r += 1
        return maxLength