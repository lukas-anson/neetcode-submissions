class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        seen = set()
        answer_list = set()

        for index, num in enumerate(nums):
            if num > 0:
                break;
            left_index = index + 1
            right_index = len(nums) - 1
            if index in seen:
                break
            while left_index < right_index:
                current_sum = num + nums[left_index] + nums[right_index]
                if current_sum > 0:
                    right_index -= 1
                elif current_sum < 0:
                    left_index += 1
                else:
                    answer_list.add((num, nums[left_index], nums[right_index]))
                    left_index += 1
                    right_index -= 1
                    

            seen.add(index)    
        
        return list(answer_list)
                    

                

