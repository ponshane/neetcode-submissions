class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_dict = {}    
        for each_str in strs:
            
            count_list = [0]*26

            for c in each_str:
                count_list[ord(c)-ord("a")] += 1

            array_key = "+".join([str(i) for i in count_list])

            if array_key not in group_dict:
                group_dict[array_key] = [each_str]
            else:
                group_dict[array_key].append(each_str)
        return [str_list for str_list in group_dict.values()]