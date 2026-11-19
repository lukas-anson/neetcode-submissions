class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums)

        # [0,1,2,3,4,5]

        while left < right:
            middle = left + ((right - left)//2)
            print(middle)

            if nums[middle] == target:
                return middle
            
            if nums[middle] < target:
                left = middle + 1

            if nums[middle] > target:
                right = middle
        return -1
        