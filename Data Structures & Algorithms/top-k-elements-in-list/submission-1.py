class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        tracker_dict = {}

        for num in nums:
            if num in tracker_dict:
                tracker_dict[num] += 1
            else:
                tracker_dict[num] = 1

        return(sorted(tracker_dict, key=lambda num: tracker_dict[num], reverse=True)[:k])
        
        