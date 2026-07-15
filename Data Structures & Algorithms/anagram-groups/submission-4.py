class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            signature = [0] * 26 # a-z
            for c in s:
                index = ord(c) - ord("a")
                signature[index] += 1
            if tuple(signature) not in res:
                res[tuple(signature)] = [s]
            else:
                res[tuple(signature)].append(s)
        return list(res.values())

            

