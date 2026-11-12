class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left_pointer = 0
        right_pointer = len(heights) - 1
        max_volume = 0

        while (left_pointer < right_pointer):
            area = min(heights[left_pointer], heights[right_pointer]) * (right_pointer - left_pointer)
            max_volume = max(max_volume, area)
            if heights[left_pointer] <= heights[right_pointer]:
                left_pointer+=1
            else:
                right_pointer-=1
        
        return max_volume
            

        
