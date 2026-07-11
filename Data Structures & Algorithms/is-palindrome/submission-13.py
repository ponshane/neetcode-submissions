class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        forward_index = 0
        backward_index = len(s) - 1
        
        while forward_index < backward_index:
            
            while (not s[forward_index].isalnum()) and (forward_index < backward_index):
                forward_index += 1

            while (not s[backward_index].isalnum()) and (backward_index > forward_index):
                backward_index -= 1

            fc = s[forward_index]
            sc = s[backward_index]
            if fc != sc:
                return False

            forward_index += 1
            backward_index -= 1
        
        return True
            
            