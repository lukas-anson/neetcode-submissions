class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set = set(nums)
        longest = 0

        for num in nums:
            if num-1 not in nums_set:
                temp_pointer = num
                temp_longest = 0
                while (temp_pointer in nums_set):
                    temp_longest += 1
                    temp_pointer +=1

                if temp_longest > longest:
                    longest = temp_longest
            else:
                continue 
                    
        return longest
