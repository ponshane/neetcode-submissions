class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        forward_index = 0
        backward_index = len(s) - 1
        first_half = ""
        second_half = ""
        
        while forward_index < backward_index:
            
            fc = s[forward_index]
            while (not fc.isalnum()) and (forward_index < len(s) - 1):
                forward_index += 1
                fc = s[forward_index]
            
            if fc.isalnum():
                first_half += fc
                forward_index += 1

            sc = s[backward_index]
            while (not sc.isalnum()) and (backward_index > 0):
                backward_index -= 1
                sc = s[backward_index]
            
            if sc.isalnum():
                second_half += sc
                backward_index -= 1

        if first_half == second_half:
            return True
        else:
            return False
            
            