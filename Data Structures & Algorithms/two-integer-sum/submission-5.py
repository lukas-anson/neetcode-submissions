class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_map = {}
        index = 0

        for num in nums:
            if (target - num) in hash_map:
                return [hash_map[target-num], index]
            else:
                hash_map[num] = index
                index+=1
        return []
                