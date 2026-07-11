class Solution:

    def encode(self, strs: List[str]) -> str:
        msg = ""
        for elem in strs:
            msg = msg + str(len(elem)) + "_" + elem
        return msg

    def decode(self, s: str) -> List[str]:
        moving_index = 0
        strs = []
        length = ""

        while moving_index < len(s):

            char = s[moving_index]

            if char == "_":
                moving_index += 1
                length_int = int(length)
                strs.append(s[moving_index:moving_index+length_int])
                moving_index += length_int
                length = ""
            else:
                moving_index += 1
                length = length + char

        return strs
            
