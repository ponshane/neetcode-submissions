class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_dict = {}
        for each_str in strs:
            str_key = "".join(sorted(each_str))
            if str_key not in group_dict:
                group_dict[str_key] = [each_str]
            else:
                group_dict[str_key].append(each_str)
        return [str_list for str_list in group_dict.values()]