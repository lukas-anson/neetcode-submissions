class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        answer_set = set()
        
        for i in range(len(nums)):
            seen = set()
            for j in range(i + 1, len(nums)):
                target = -(nums[i] + nums[j])
                if target in seen:
                    triplet = tuple(sorted([nums[i], nums[j], target]))
                    answer_set.add(triplet)
                seen.add(nums[j])
                
        return [list(triplet) for triplet in answer_set]
