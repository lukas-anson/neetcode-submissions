class Solution:
    def isPalindrome(self, s: str) -> bool:

        s_with_space = "".join(char.lower() for char in s if char.isalnum())
        s_in_list = list(s_with_space);
        print(s_in_list)
        front = 0
        back = len(s_in_list) - 1

        while (front < back):
            if s_in_list[front] != s_in_list[back]:
                return False
            front+=1
            back-=1
        
        return True