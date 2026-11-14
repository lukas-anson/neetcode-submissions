class Solution:
    def isPalindrome(self, s: str) -> bool:

        # s_with_space = "".join(char.lower() for char in s if char.isalnum())

        # return s_with_space == s_with_space[::-1]


        s_with_space = "".join(char.lower() for char in s if char.isalnum())

        return s_with_space == s_with_space[::-1]