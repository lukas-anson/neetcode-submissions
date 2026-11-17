class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        letter_count = {}
        l = 0
        longest_substring = 0


        for r in range(len(s)):
            letter_count[s[r]] = 1 + letter_count.get(s[r], 0)
            
            while (r - l + 1) - max(letter_count.values()) > k:
                letter_count[s[l]] -= 1
                l += 1
            longest_substring = max(longest_substring, (r - l + 1))
        
        return longest_substring

