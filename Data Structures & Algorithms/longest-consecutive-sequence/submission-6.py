class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # [2,20,4,10,3,4,5]
        nums_set = set(nums)
        longest = 0

        if len(nums) == 0:
            return 0;
 
        for num in nums_set:
            if num - 1 not in nums_set:
                local_longest = 0
                flag = True
    
                while flag:
                    if num+1 in nums_set:
                        local_longest+=1
                        num+=1
                    else:
                        longest = max(longest, local_longest)
                        flag = False
        return longest + 1