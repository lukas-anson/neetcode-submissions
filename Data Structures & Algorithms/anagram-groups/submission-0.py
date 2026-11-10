class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        output_list = []
        hash_map = {}

        for string in strs:
            sorted_string = "".join(sorted(string))
            if sorted_string in hash_map:
                hash_map[sorted_string].append(string)
            else:
                hash_map[sorted_string] = [string]
        
        for key in hash_map:
            output_list.append(hash_map[key])
        return output_list