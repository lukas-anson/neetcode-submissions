class Solution:
    def trap(self, height: List[int]) -> int:

        total_water = 0 
        prefix_array = []
        postfix_array = []

        prev_max = 0
        for value in height:
            prefix_array.append(prev_max)
            prev_max = max(prev_max, value)

        post_max = 0
        for value in reversed(height):
            postfix_array.append(post_max)
            post_max = max(post_max, value)

        postfix_array.reverse()

        for i in range(len(height)):
            local_water = min(prefix_array[i], postfix_array[i]) - height[i]

            if local_water >= 0:
                total_water += local_water


        return total_water