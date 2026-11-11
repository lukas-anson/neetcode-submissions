class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1,2,4,6] 
        #[6,4,2,1]

        # [1,1,2,8]
        # [48,24,6,1]

        res = [1] * (len(nums))

        # [1,1,1,1]

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res

            

        

