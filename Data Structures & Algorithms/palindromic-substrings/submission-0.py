class Solution:
    def countSubstrings(self, s: str) -> int:
        numPalindromes = 0

        # two pointers solution
        for i in range(len(s)):

            # for odd length palindrome
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                numPalindromes += 1
                l -= 1
                r += 1
            
            # for even length palindrome
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                numPalindromes += 1
                l -= 1
                r += 1
        
        return numPalindromes