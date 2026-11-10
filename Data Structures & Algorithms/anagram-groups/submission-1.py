class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hash_map = {}
        answer_array = []

        for string in strs:
            key = "".join(sorted(string))
            if key in hash_map:
                hash_map[key].append(string)
            else:
                hash_map[key] = [string]
            
        for key in hash_map:
            answer_array.append(hash_map[key])

        return answer_array
