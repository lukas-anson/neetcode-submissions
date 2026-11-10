class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # before = [1,1,2,8]
        # after = [48,24,6,1]

        forward = []
        back = []

        curr_forward = 1
        for i in range(len(nums)):
            forward.append(curr_forward)
            curr_forward *= nums[i]

        curr_back = 1
        for num in reversed(nums):
            back.append(curr_back)
            curr_back *= num

        for k in range(len(forward)):
            forward[k] *= back[len(back) - k - 1]
        
        return forward



            