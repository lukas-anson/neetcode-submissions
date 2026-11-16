class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        hash_set = set()
        left_pointer = 0
        longest = 0
        

        for right_pointer in range(len(s)):
            while s[right_pointer] in hash_set:
                hash_set.remove(s[left_pointer])
                left_pointer += 1
            longest = max(longest, right_pointer - left_pointer + 1)
            hash_set.add(s[right_pointer])
        return longest