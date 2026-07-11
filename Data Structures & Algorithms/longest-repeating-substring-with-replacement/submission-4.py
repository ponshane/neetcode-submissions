class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        n = len(s)
        count = {}
        l, res, maxfreq = 0, 0, 0

        for r in range(n):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxfreq = max(maxfreq, count[s[r]])

            # if (r-l+1) - maxfreq > k => also works
            while (r-l+1) - maxfreq > k:
                count[s[l]] -=1
                l += 1
                # think about why maxfreq does not have to be decreased

            res = max(r-l+1, res)
        
        return res