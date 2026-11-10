class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hash_table = {}
        answer = []

        for num in nums:
            if num in hash_table:
                hash_table[num] += 1
            else:
                hash_table[num] = 1
        
        answer = sorted(hash_table, key=hash_table.get, reverse=True)
        return answer[0:k]
