class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # AAABABB
        letter_map = {}
        longest_substring = 0
        left_pointer = 0
        
        # (right_pointer - left_pointer) - most_freq_in_window <= k

        most_freq_in_window = 0
        for right_pointer in range(len(s)):
            letter_map[s[right_pointer]] = 1 + letter_map.get(s[right_pointer], 0)
            most_freq_in_window = max(most_freq_in_window, letter_map[s[right_pointer]])

            while (right_pointer - left_pointer + 1) - most_freq_in_window > k:
                letter_map[s[left_pointer]] -= 1
                left_pointer += 1 
            longest_substring = max(longest_substring, right_pointer - left_pointer + 1)

        return longest_substring
                


