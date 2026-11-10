class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hash_map = {}
        result_list = []

        for num in nums:
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1
        
        for i in range(k):
            largest_value = max(hash_map, key=hash_map.get)
            result_list.append(largest_value)
            hash_map.pop(largest_value)
        return result_list
            
            
            
